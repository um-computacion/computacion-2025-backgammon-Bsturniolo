
import pytest
from core.board import Board

def test_cannot_move_into_blocked_point_by_two_or_more():
    b = Board()
    # Punto 11 tiene +5 de J1; simulemos que mueve J2 desde 12 -> 11 (bloqueado)
    assert b.can_move(12, 11) is False

def test_hit_sends_enemy_to_bar_and_places_owner():
    b = Board()
    # Punto 0 tiene +2 de J1; dejemos 1 solo rival en 1 para que J1 golpee
    b.get_points()[1] = -1
    b.move_checker(0, 1)
    assert b.get_bar()[-1] == 1     # rival a la barra
    assert b.get_points()[1] == 1   # queda 1 del owner

def test_invalid_indices_and_empty_origin():
    b = Board()
    with pytest.raises(ValueError):
        b.move_checker(-1, 0)
    with pytest.raises(ValueError):
        b.move_checker(0, 24)
    # Vaciar origen y probar
    b.get_points()[16] = 0
    with pytest.raises(ValueError):
        b.move_checker(16, 17)
