"""Federated Learning client for local training."""
from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class FLClient:
    """Client that trains locally and sends updates to the server."""

    def __init__(self, client_id: str) -> None:
        self.client_id = client_id
        self._weights: list[float] = [0.0, 0.0, 0.0]

    def train(self, data: list[float]) -> list[float]:
        """Simulate local training and return updated weights."""
        self._weights = [w + d * 0.01 for w, d in zip(self._weights, data)]
        logger.info("Client %s trained, weights: %s", self.client_id, self._weights)
        return self._weights

    def get_weights(self) -> list[float]:
        """Return current model weights."""
        return list(self._weights)
