import unittest
from core.board import Board

class TestBoardBar(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_bar_starts_empty(self):
        bar = self.board.get_bar()
        self.assertEqual(bar[1], 0)
        self.assertEqual(bar[-1], 0)

    def test_hit_sends_checker_to_bar(self):
        board = Board()
        # Punto 0 tiene fichas del jugador 1 (positivas)
        # Punto 1 tendrá una sola ficha del jugador 2 (negativa)
        board.get_points()[1] = -1

        board.move_checker(0, 1)

        # La ficha enemiga debería ir a la barra del jugador 2 (-1)
        self.assertEqual(board.get_bar()[-1], 1)

        # El destino ahora debe tener una ficha del jugador 1
        self.assertEqual(board.get_points()[1], 1)

    def test_normal_move_does_not_affect_bar(self):
        board = Board()
        initial_bar = board.get_bar().copy()

        board.move_checker(0, 1)  # Movimiento normal (sin golpe)
        self.assertEqual(board.get_bar(), initial_bar)

    def test_invalid_move_does_not_change_bar(self):
        board = Board()
        initial_bar = board.get_bar().copy()
        with self.assertRaises(ValueError):
            board.move_checker(0, 5)  # Punto 6 bloqueado
        self.assertEqual(board.get_bar(), initial_bar)

if __name__ == "__main__":
    unittest.main()
