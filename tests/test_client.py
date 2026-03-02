"""Tests for the FL client."""
from src.client import FLClient


def test_train_updates_weights() -> None:
    c = FLClient("node-1")
    result = c.train([100.0, 200.0, 300.0])
    assert result == [1.0, 2.0, 3.0]


def test_get_weights_returns_copy() -> None:
    c = FLClient("node-2")
    w = c.get_weights()
    w[0] = 999.0
    assert c.get_weights()[0] == 0.0


def test_client_id_stored() -> None:
    c = FLClient("dept-a")
    assert c.client_id == "dept-a"
