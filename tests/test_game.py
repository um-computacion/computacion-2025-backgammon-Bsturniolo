
import builtins
import types

from core.game import BackgammonGame

class DummyDice:
    """Dado determinístico para tests."""
    def __init__(self, seq):
        # seq puede ser [a,b] (normal) o [d,d,d,d] (doble expandido)
        self._seq = list(seq)
    def roll(self):
        return list(self._seq)

def test_board_initial_setup_and_bar_empty():
    g = BackgammonGame()
    pts = g.get_points()
    bar = g.get_bar()
    # 24 puntos
    assert isinstance(pts, list) and len(pts) == 24
    # barra vacía
    assert bar.get(1, None) == 0
    assert bar.get(-1, None) == 0
    # posiciones iniciales básicas (sanity)
    # Jugador 1
    assert pts[0] == 2
    assert pts[11] == 5
    assert pts[16] == 3
    assert pts[18] == 5
    # Jugador -1
    assert pts[23] == -2
    assert pts[12] == -5
    assert pts[7]  == -3
    assert pts[5]  == -5

def test_roll_dice_normal_returns_two_values():
    g = BackgammonGame()
    # inyectamos un dado determinístico [3,5]
    g.set_dice(DummyDice([3, 5]))

    vals = g.roll_dice()
    assert vals == [3, 5]
    assert g.get_available_moves() == [3, 5]

def test_roll_dice_double_returns_four_values():
    g = BackgammonGame()
    # doble 4 -> ya expandido a 4 movimientos
    g._BackgammonGame__dice__ = DummyDice([4, 4, 4, 4])
    vals = g.roll_dice()
    assert vals == [4, 4, 4, 4]
    assert g.get_available_moves() == [4, 4, 4, 4]

def test_change_turn_switches_current_player():
    g = BackgammonGame("P1", "P2")
    p1 = g.current_player()
    g.change_turn()
    p2 = g.current_player()
    assert p1 is not p2
