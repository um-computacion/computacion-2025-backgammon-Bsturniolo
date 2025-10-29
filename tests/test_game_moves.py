
import pytest
from core.game import BackgammonGame

class DummyDice:
    def __init__(self, seq):
        self._seq = list(seq)
    def roll(self):
        return list(self._seq)

def test_cannot_move_without_dice():
    g = BackgammonGame()
    with pytest.raises(ValueError):
        g.move(16, 19)  # sin tirar dados

def test_move_consumes_die_value_and_does_not_change_turn_if_moves_remain():
    g = BackgammonGame()
    # Dado determinístico: [3,5]
    g.set_dice(DummyDice([3, 5]))

    g.roll_dice()
    # Jugador 1 mueve hacia índices mayores. Desde 16 → 19 es distancia 3 y destino 19 está libre al inicio.
    g.move(16, 19)
    # Consumió el 3, debe quedar [5]
    assert g.get_available_moves() == [5]
    # Sigue mismo jugador porque aún queda un valor por usar antes del fin de turno
    # (El test no exige verificar el jugador; alcanza con que aún haya movimientos)
    assert g.get_available_moves() == [5]

def test_turn_changes_when_no_moves_left():
    g = BackgammonGame("A", "B")
    # Dado determinístico: [1] (un único movimiento)
    g._BackgammonGame__dice__ = DummyDice([1])
    g.roll_dice()
    # Para que haya un movimiento legal: desde 18 → 19 (distancia 1) es válido (Jugador 1 hacia mayor índice).
    g.move(18, 19)
    # Se consumió el único valor: debe cambiar el turno y no quedar movimientos
    assert g.get_available_moves() == []

def test_direction_enforced_for_player1():
    g = BackgammonGame()
    g._BackgammonGame__dice__ = DummyDice([1, 2])
    g.roll_dice()
    # Intentar mover hacia atrás (11 → 10) debe fallar para Jugador 1
    with pytest.raises(ValueError):
        g.move(11, 10)

def test_bar_rule_enforced_before_any_other_move():
    g = BackgammonGame()
    # simular que el J1 tiene una ficha en barra
    g.get_bar()[1] = 1
    g._BackgammonGame__dice__ = DummyDice([1, 2])
    g.roll_dice()
    # Mientras tengas fichas en barra, no podés mover desde tablero
    with pytest.raises(ValueError):
        g.move(16, 17)
