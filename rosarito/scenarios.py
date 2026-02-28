"""Steady-state staging scenarios and 24h EPS with pump trips.

Each scenario loads a fresh epanet object to avoid state leakage.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from epyt import epanet

from rosarito.constants import (
    INP_FILE,
    DUTY_PUMP_IDS,
    STANDBY_PUMP_ID,
    PUMP_IDS,
    RIKO_IDS,
    RIKO_OPENINGS,
    RIKO_BY_NPUMPS,
    PIPE_IDS,
    JUNCTION_IDS,
    RESERVOIR_IDS,
    RikoOpening,
)
from rosarito.model import SteadyStateResult, EPSResult


def _build_name_index_maps(
    d: epanet,
) -> tuple[dict[str, int], dict[str, int]]:
    """Build name→index dicts for links and nodes."""
    link_names = d.getLinkNameID()
    link_idx = {name: i for i, name in enumerate(link_names, start=1)}
    node_names = d.getNodeNameID()
    node_idx = {name: i for i, name in enumerate(node_names, start=1)}
    return link_idx, node_idx


# ---------------------------------------------------------------------------
# Steady-state staging
# ---------------------------------------------------------------------------

def run_staging_scenarios(
    inp_path: str | Path | None = None,
) -> list[SteadyStateResult]:
    """Run all 4 staging scenarios (4-pump down to 1-pump).

    Each scenario uses a fresh EPyT instance and a duration-0 simulation.
    Returns a list of SteadyStateResult ordered from 4 pumps to 1 pump.
    """
    path = str(inp_path or INP_FILE)
    results: list[SteadyStateResult] = []

    for opening in RIKO_OPENINGS:
        result = _run_single_scenario(path, opening)
        results.append(result)

    return results


def _run_single_scenario(
    inp_path: str, opening: RikoOpening,
) -> SteadyStateResult:
    """Run a single steady-state scenario for the given RIKO opening."""
    d = epanet(inp_path)

    try:
        link_idx, node_idx = _build_name_index_maps(d)

        # Single hydraulic timestep (steady state)
        d.setTimeSimulationDuration(0)

        # Configure pump statuses: first N duty pumps OPEN, rest CLOSED
        _configure_pumps(d, link_idx, opening.n_pumps)

        # Configure RIKO GPVs: only the correct one OPEN
        _configure_riko(d, link_idx, opening)

        # Run hydraulic simulation
        ts = d.getComputedHydraulicTimeSeries()

        # Extract results from the single timestep (index 0)
        result = _extract_results(d, ts, link_idx, node_idx, opening)

    finally:
        d.unload()

    return result


def _configure_pumps(
    d: epanet, link_idx: dict[str, int], n_active: int,
) -> None:
    """Set initial status: first n_active duty pumps OPEN, rest CLOSED."""
    for i, pump_id in enumerate(DUTY_PUMP_IDS):
        status = 1 if i < n_active else 0  # 1=OPEN, 0=CLOSED
        d.setLinkInitialStatus(link_idx[pump_id], status)

    # Standby always CLOSED for steady-state scenarios
    d.setLinkInitialStatus(link_idx[STANDBY_PUMP_ID], 0)


def _configure_riko(
    d: epanet, link_idx: dict[str, int], active_opening: RikoOpening,
) -> None:
    """Open only the GPV for the active opening, close all others."""
    for riko_id in RIKO_IDS:
        status = 1 if riko_id == active_opening.gpv_link_id else 0
        d.setLinkInitialStatus(link_idx[riko_id], status)


def _extract_results(
    d: epanet,
    ts,
    link_idx: dict[str, int],
    node_idx: dict[str, int],
    opening: RikoOpening,
) -> SteadyStateResult:
    """Extract hydraulic results from the computed time series."""
    # Flow through downstream pipe = total system flow
    q_total = float(ts.Flow[0, link_idx["P_DS"] - 1])

    # Heads at key nodes (EPyT uses 0-based column indices in ts arrays)
    h_suction = float(ts.Head[0, node_idx["J_SUCTION"] - 1])
    h_manifold = float(ts.Head[0, node_idx["J_MANIFOLD"] - 1])
    h_riko_in = float(ts.Head[0, node_idx["J_RIKO_IN"] - 1])
    h_riko_out = float(ts.Head[0, node_idx["J_RIKO_OUT"] - 1])

    # Pump head = discharge head - suction head
    h_pump = h_manifold - h_suction

    # RIKO headloss
    dh_riko = h_riko_in - h_riko_out

    # Flow per pump
    q_per_pump = q_total / opening.n_pumps

    # Pipe velocities and headlosses
    velocities = {}
    headlosses = {}
    for pipe_id in PIPE_IDS:
        idx = link_idx[pipe_id] - 1
        velocities[pipe_id] = float(ts.Velocity[0, idx])
        headlosses[pipe_id] = float(ts.HeadLoss[0, idx])

    return SteadyStateResult(
        n_active_pumps=opening.n_pumps,
        riko_opening_pct=opening.phi_pct,
        q_total_lps=q_total,
        q_per_pump_lps=q_per_pump,
        h_pump_m=h_pump,
        dh_riko_m=dh_riko,
        h_suction=h_suction,
        h_manifold=h_manifold,
        h_riko_in=h_riko_in,
        h_riko_out=h_riko_out,
        pipe_velocities=velocities,
        pipe_headlosses=headlosses,
    )


# ---------------------------------------------------------------------------
# Extended Period Simulation (EPS) with pump trips
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PumpTripEvent:
    """A scheduled pump trip and restore during EPS."""
    pump_id: str
    trip_hour: float       # hour to trip (close) pump
    restore_hour: float    # hour to restore (open) pump


DEFAULT_PUMP_TRIPS: list[PumpTripEvent] = [
    PumpTripEvent("PUMP_4", trip_hour=6.0,  restore_hour=8.0),
    PumpTripEvent("PUMP_3", trip_hour=12.0, restore_hour=14.0),
    PumpTripEvent("PUMP_2", trip_hour=18.0, restore_hour=20.0),
]


def run_eps_with_trips(
    inp_path: str | Path | None = None,
    trips: list[PumpTripEvent] | None = None,
) -> EPSResult:
    """Run 24h EPS with scheduled pump trips.

    Pump trips are added as EPANET simple controls (per Project Instructions
    Section 7: add to [CONTROLS], never modify [RULES]).
    The rule-based controls in the INP handle standby activation and valve
    position changes automatically.
    """
    path = str(inp_path or INP_FILE)
    if trips is None:
        trips = DEFAULT_PUMP_TRIPS

    d = epanet(path)

    try:
        link_idx, node_idx = _build_name_index_maps(d)

        # Add pump trip/restore controls
        for trip in trips:
            trip_seconds = int(trip.trip_hour * 3600)
            restore_seconds = int(trip.restore_hour * 3600)

            # EPyT addControls format: 'LINK <id> <status> AT TIME <seconds>'
            d.addControls(f"LINK {trip.pump_id} 0 AT TIME {trip_seconds}")
            d.addControls(f"LINK {trip.pump_id} 1 AT TIME {restore_seconds}")

        # Run full 24h EPS
        ts = d.getComputedHydraulicTimeSeries()

        # Extract time series for all tracked elements
        time_s = ts.Time.tolist()

        all_link_ids = PUMP_IDS + RIKO_IDS + PIPE_IDS
        all_node_ids = JUNCTION_IDS + RESERVOIR_IDS

        flows: dict[str, list[float]] = {}
        velocities: dict[str, list[float]] = {}
        statuses: dict[str, list[int]] = {}
        for lid in all_link_ids:
            idx = link_idx[lid] - 1
            flows[lid] = ts.Flow[:, idx].tolist()
            velocities[lid] = ts.Velocity[:, idx].tolist()
            statuses[lid] = [int(s) for s in ts.Status[:, idx].tolist()]

        heads: dict[str, list[float]] = {}
        for nid in all_node_ids:
            idx = node_idx[nid] - 1
            heads[nid] = ts.Head[:, idx].tolist()

    finally:
        d.unload()

    return EPSResult(
        time_s=time_s,
        flows=flows,
        heads=heads,
        velocities=velocities,
        statuses=statuses,
    )


def run_eps_baseline(
    inp_path: str | Path | None = None,
) -> EPSResult:
    """Run 24h EPS with no pump trips (baseline: 4 duty pumps, RIKO at 44%)."""
    return run_eps_with_trips(inp_path, trips=[])
