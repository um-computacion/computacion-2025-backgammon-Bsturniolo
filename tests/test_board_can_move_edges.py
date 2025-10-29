
from core.board import Board

def test_can_move_invalid_indices_returns_false():
    b = Board()
    assert b.can_move(-1, 0) is False
    assert b.can_move(0, 24) is False

def test_can_move_empty_origin_returns_false():
    b = Board()
    b.get_points()[16] = 0
    assert b.can_move(16, 17) is False
