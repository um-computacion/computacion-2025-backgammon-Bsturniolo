
import pytest
from core.board import Board

def test_reentry_blocked_by_two_or_more():
    b = Board()
    # J1 intenta entrar en idx=5, que en el inicio tiene -5 (bloqueado)
    b.get_bar()[1] = 1
    with pytest.raises(ValueError):
        b.reenter_from_bar(1, 5)

def test_reentry_invalid_owner_or_point():
    b = Board()
    b.get_bar()[1] = 1
    with pytest.raises(ValueError):
        b.reenter_from_bar(3, 0)  # owner inválido
    with pytest.raises(ValueError):
        b.reenter_from_bar(1, 24)  # punto inválido
