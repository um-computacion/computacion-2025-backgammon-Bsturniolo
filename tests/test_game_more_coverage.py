
import pytest
from core.game import BackgammonGame

class DummyDice:
    def __init__(self, seq): self._seq = list(seq)
    def roll(self): return list(self._seq)

def test_set_dice_injection_and_roll():
    g = BackgammonGame()
    g.set_dice(DummyDice([2, 3]))
    assert g.roll_dice() == [2, 3]

def test_reenter_without_bar_raises():
    g = BackgammonGame()
    # Nadie en barra: debe fallar
    with pytest.raises(ValueError):
        g.reenter(0)

def test_move_origin_empty_raises():
    g = BackgammonGame()
    g.set_dice(DummyDice([1]))
    g.roll_dice()
    # Vaciamos un punto y tratamos de mover desde ahí → tablero lo rechaza
    g.get_points()[16] = 0
    with pytest.raises(ValueError):
        g.move(16, 17)

def test_is_forward_invalid_owner_returns_false():
    # Llama al helper estático con owner inválido (cubre rama de retorno False)
    assert BackgammonGame._is_forward(0, 5, 6) is False
