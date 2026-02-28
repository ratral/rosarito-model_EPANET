"""Shared helpers for EPS event-log processing.

Used by both reporting.py (console tables) and report.py (Markdown output)
to avoid duplicating the timestep iteration and change-detection logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

from rosarito.constants import PUMP_IDS, RIKO_IDS, lps_to_m3h
from rosarito.model import EPSResult


def format_sim_time(seconds: float) -> tuple[int, int]:
    """Convert simulation seconds to (hours, minutes)."""
    hours = seconds / 3600.0
    h = int(hours)
    m = int((hours - h) * 60)
    return h, m


def riko_label(riko_id: str) -> str:
    """Convert EPANET GPV ID to display label: 'RIKO_44' -> '44%'."""
    return riko_id.replace("RIKO_", "") + "%"


@dataclass
class EPSEventRow:
    """One row in the EPS event log (emitted only when state changes)."""
    time_s: float
    hours: int
    minutes: int
    pump_on: list[bool]
    n_active: int
    riko_opening: str       # e.g. "44%" or "---"/"—"
    q_ds_lps: float
    q_ds_m3h: float
    h_pump_m: float


def iter_eps_events(eps: EPSResult) -> Iterator[EPSEventRow]:
    """Iterate EPS timesteps, yielding a row only when state changes.

    Yields the first timestep, every timestep where pump status or RIKO
    opening differs from the previous one, and the last timestep.
    """
    prev_pump_states: list[int] | None = None
    prev_riko_open: str | None = None

    for i, t_s in enumerate(eps.time_s):
        pump_states = [eps.statuses[pid][i] for pid in PUMP_IDS]
        n_active = sum(1 for s in pump_states if s != 0)

        riko_open = "---"
        for rid in RIKO_IDS:
            if eps.statuses[rid][i] != 0:
                riko_open = riko_label(rid)

        changed = (
            prev_pump_states is None
            or pump_states != prev_pump_states
            or riko_open != prev_riko_open
            or i == len(eps.time_s) - 1
        )

        if changed:
            h, m = format_sim_time(t_s)

            q_ds = eps.flows["P_DS"][i]
            q_m3h = lps_to_m3h(q_ds)

            h_manifold = eps.heads["J_MANIFOLD"][i]
            h_suction = eps.heads["J_SUCTION"][i]
            h_pump = h_manifold - h_suction

            yield EPSEventRow(
                time_s=t_s,
                hours=h,
                minutes=m,
                pump_on=[s != 0 for s in pump_states],
                n_active=n_active,
                riko_opening=riko_open,
                q_ds_lps=q_ds,
                q_ds_m3h=q_m3h,
                h_pump_m=h_pump,
            )

        prev_pump_states = pump_states[:]
        prev_riko_open = riko_open
