
import pytest
from core.game import BackgammonGame

class DummyDice:
    def __init__(self, seq): self._seq = list(seq)
    def roll(self): return list(self._seq)

def test_move_without_available_moves_raises():
    g = BackgammonGame()
    # Sin tirar dados → cubre "No hay movimientos disponibles." (línea ~70)
    with pytest.raises(ValueError):
        g.move(16, 17)

def test_change_turn_clears_available_moves():
    g = BackgammonGame()
    g.set_dice(DummyDice([2]))
    g.roll_dice()
    assert g.get_available_moves() == [2]
    g.change_turn()  # cubre línea ~112 (clear de movimientos)
    assert g.get_available_moves() == []

def test_reenter_requires_matching_die_value():
    g = BackgammonGame()
    # poner 1 ficha de J1 en barra
    g.get_bar()[1] = 1
    # dado = 2 → intenta reingresar en entry_point 0 (distancia esperada para J1 = 1)
    g.set_dice(DummyDice([2]))
    g.roll_dice()
    with pytest.raises(ValueError):
        g.reenter(0)  # “El valor de dado no permite reingresar en ese punto.” (132–140)

def test_reenter_success_consumes_die_and_may_change_turn():
    g = BackgammonGame()
    g.get_bar()[1] = 1
    # Para J1, entry_point 1 requiere distancia 2 → usamos [2]
    g.set_dice(DummyDice([2]))
    g.roll_dice()
    g.reenter(1)      # debería consumir el dado
    assert g.get_available_moves() == []  # sin movimientos → turn cambia internamente (línea 143)
