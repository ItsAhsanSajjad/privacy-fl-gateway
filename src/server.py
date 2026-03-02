"""Federated Learning aggregation server."""
from __future__ import annotations

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


class FLServer:
    """Lightweight FL server for coordinating training rounds."""

    def __init__(self, num_rounds: int = 5, min_clients: int = 2) -> None:
        self.num_rounds = num_rounds
        self.min_clients = min_clients
        self._round = 0

    def aggregate(self, updates: list[list[float]]) -> list[float]:
        """Aggregate model updates using FedAvg."""
        if not updates:
            return []
        n = len(updates)
        dim = len(updates[0])
        return [sum(u[i] for u in updates) / n for i in range(dim)]

    def run_round(self, updates: list[list[float]]) -> list[float]:
        """Execute a single training round."""
        self._round += 1
        logger.info("Round %d: aggregating %d updates", self._round, len(updates))
        return self.aggregate(updates)


if __name__ == "__main__":
    server = FLServer()
    dummy = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    result = server.run_round(dummy)
    logger.info("Aggregated weights: %s", result)
