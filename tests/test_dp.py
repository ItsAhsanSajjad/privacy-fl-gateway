"""Tests for the dIfferential privacy strategy."""
from src.strategy.dp import DPStrategy
import pytest


def test_apply_adds_noise() -> None:
    dp = DPStrategy(epsilon=1.0)
    original = [1.0, 2.0, 3.0]
    noisy = dp.apply(original)
    assert len(noisy) == len(original)
    assert noisy != original  # Extremely unlikely to be identical


def test_invalid_epsilon_raises() -> None:
    with pytest.raises(ValueError):
        DPStrategy(epsilon=0)


def test_privacy_budget() -> None:
    dp = DPStrategy()
    assert dp.privacy_budget_remaining(3, 10) == pytest.approx(0.7)
    assert dp.privacy_budget_remaining(10, 10) == 0.0
