"""Differential privacy strategy for federated learning."""
from __future__ import annotations

import random
import math


class DPStrategy:
    """Applies calibrated Laplace noise for (epsilon)-differential privacy."""

    def __init__(self, epsilon: float = 1.0, sensitivity: float = 1.0) -> None:
        if epsilon <= 0:
            raise ValueError("Epsilon must be positive")
        self.epsilon = epsilon
        self.sensitivity = sensitivity

    def _laplace_noise(self) -> float:
        """Generate a single Laplace noise sample."""
        scale = self.sensitivity / self.epsilon
        u = random.random() - 0.5
        return -scale * math.copysign(1, u) * math.log(1 - 2 * abs(u))

    def apply(self, weights: list[float]) -> list[float]:
        """Add calibrated noise to model weights."""
        return [w + self._laplace_noise() for w in weights]

    def privacy_budget_remaining(self, rounds_used: int, total_rounds: int) -> float:
        """Return fraction of privacy budget remaining."""
        if total_rounds <= 0:
            return 0.0
        return max(0.0, 1.0 - rounds_used / total_rounds)
