"""RosaritoModel — EPyT wrapper with domain-specific accessors.

Loads the EPANET INP file via EPyT and provides convenient access
to pumps, valves, pipes, and nodes by their engineering IDs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from epyt import epanet

from rosarito.constants import (
    INP_FILE,
    PUMP_IDS,
    RIKO_IDS,
    PIPE_IDS,
    JUNCTION_IDS,
    RESERVOIR_IDS,
)


@dataclass
class SteadyStateResult:
    """Hydraulic results for one staging scenario."""
    n_active_pumps: int
    riko_opening_pct: int
    q_total_lps: float
    q_per_pump_lps: float
    h_pump_m: float
    dh_riko_m: float
    h_suction: float
    h_manifold: float
    h_riko_in: float
    h_riko_out: float
    pipe_velocities: dict[str, float] = field(default_factory=dict)
    pipe_headlosses: dict[str, float] = field(default_factory=dict)


@dataclass
class EPSResult:
    """Time-series results from an extended period simulation."""
    time_s: list[float]
    flows: dict[str, list[float]]       # link_id → [flow at each timestep]
    heads: dict[str, list[float]]       # node_id → [head at each timestep]
    velocities: dict[str, list[float]]  # link_id → [velocity at each timestep]
    statuses: dict[str, list[int]]      # link_id → [status at each timestep]


class RosaritoModel:
    """Manages EPyT lifecycle and provides domain accessors."""

    def __init__(self, inp_path: str | Path | None = None):
        self.inp_path = str(inp_path or INP_FILE)
        self._d: epanet | None = None
        self._link_name_to_idx: dict[str, int] = {}
        self._node_name_to_idx: dict[str, int] = {}

    def load(self) -> epanet:
        """Load the INP file and build name→index maps. Returns the epanet object."""
        self._d = epanet(self.inp_path)
        self._build_index_maps()
        return self._d

    def _build_index_maps(self) -> None:
        d = self._d
        link_names = d.getLinkNameID()
        for i, name in enumerate(link_names, start=1):
            self._link_name_to_idx[name] = i
        node_names = d.getNodeNameID()
        for i, name in enumerate(node_names, start=1):
            self._node_name_to_idx[name] = i

    @property
    def d(self) -> epanet:
        if self._d is None:
            raise RuntimeError("Model not loaded. Call load() first.")
        return self._d

    def close(self) -> None:
        if self._d is not None:
            self._d.unload()
            self._d = None

    def __enter__(self) -> RosaritoModel:
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    # --- Index accessors ---

    def link_index(self, link_id: str) -> int:
        return self._link_name_to_idx[link_id]

    def node_index(self, node_id: str) -> int:
        return self._node_name_to_idx[node_id]

    def pump_index(self, pump_id: str) -> int:
        return self.link_index(pump_id)

    def riko_index(self, riko_id: str) -> int:
        return self.link_index(riko_id)

    def pipe_index(self, pipe_id: str) -> int:
        return self.link_index(pipe_id)
