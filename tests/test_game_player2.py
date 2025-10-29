
import pytest
from core.game import BackgammonGame

class DummyDice:
    def __init__(self, seq):
        self._seq = list(seq)
    def roll(self):
        return list(self._seq)

def test_player2_moves_left_and_turn_changes():
    g = BackgammonGame("A", "B")
    g.change_turn()  # pasa a Jugador 2 (id = -1)

    # Dado determinístico: [1]
    g.set_dice(DummyDice([1]))
    g.roll_dice()

    # Estado inicial: J2 tiene -3 en idx=7, idx=6 está libre -> mover 7 -> 6 (distancia 1) es válido
    g.move(7, 6)
    # Consumió el único valor -> sin movimientos
    assert g.get_available_moves() == []

def test_player2_wrong_direction_raises():
    g = BackgammonGame()
    g.change_turn()  # Jugador 2
    g.set_dice(DummyDice([1, 2]))
    g.roll_dice()
    # Intentar ir hacia la derecha (7 -> 8) es inválido para J2
    with pytest.raises(ValueError):
        g.move(7, 8)
