"""Tests for the FL server."""
from src.server import FLServer


def test_aggregate_averages_weights() -> None:
    server = FLServer()
    result = server.aggregate([[1.0, 2.0], [3.0, 4.0]])
    assert result == [2.0, 3.0]


def test_aggregate_empty_returns_empty() -> None:
    server = FLServer()
    assert server.aggregate([]) == []


def test_run_round_increments_counter() -> None:
    server = FLServer()
    server.run_round([[1.0]])
    server.run_round([[2.0]])
    assert server._round == 2
