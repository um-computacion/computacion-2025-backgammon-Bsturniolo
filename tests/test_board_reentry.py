import unittest
from core.board import Board

class TestBoardReentry(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_reentry_reduces_bar_count(self):
        """Verifica que al reingresar una ficha, se reduzca la barra."""
        self.board.get_bar()[1] = 1  # Jugador 1 tiene una ficha en barra
        self.board.reenter_from_bar(1, 0)
        self.assertEqual(self.board.get_bar()[1], 0)
        self.assertEqual(self.board.get_points()[0], 3)  # Punto inicial tenía 2, ahora 3

    def test_reentry_onto_empty_point(self):
        """Verifica que la ficha se agregue correctamente en un punto vacío."""
        self.board.get_bar()[1] = 1
        self.board.get_points()[2] = 0
        self.board.reenter_from_bar(1, 2)
        self.assertEqual(self.board.get_points()[2], 1)

    def test_reentry_hits_enemy_checker(self):
        """Si el punto tiene una ficha enemiga solitaria, se la golpea."""
        self.board.get_bar()[1] = 1
        self.board.get_points()[1] = -1  # ficha enemiga solitaria
        self.board.reenter_from_bar(1, 1)
        self.assertEqual(self.board.get_points()[1], 1)   # reemplazada por jugador 1
        self.assertEqual(self.board.get_bar()[-1], 1)     # ficha golpeada va a barra enemiga

    def test_reentry_blocked_point_raises_error(self):
        """No se puede reingresar si el punto está bloqueado."""
        self.board.get_bar()[1] = 1
        self.board.get_points()[1] = -2  # punto bloqueado
        with self.assertRaises(ValueError):
            self.board.reenter_from_bar(1, 1)

    def test_cannot_reenter_if_bar_empty(self):
        """No se puede reingresar si no hay fichas en la barra."""
        with self.assertRaises(ValueError):
            self.board.reenter_from_bar(1, 0)

if __name__ == "__main__":
    unittest.main()
