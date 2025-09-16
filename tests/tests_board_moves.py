import unittest
from core.board import Board

class TestBoardMoves(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_move_checker_valid(self):
        # Mover una ficha del punto 1 (índice 0) al punto 2 (índice 1)
        self.board.move_checker(0, 1)
        self.assertEqual(self.board.get_points()[0], 1)   # queda 1 en el origen
        self.assertEqual(self.board.get_points()[1], 1)   # aparece 1 en el destino

    def test_move_checker_from_empty_point_raises(self):
        with self.assertRaises(ValueError):
            self.board.move_checker(3, 4)  # punto 4 arranca vacío en la posición inicial

    def test_move_checker_blocked_point_raises(self):
        # Intentar mover del punto 1 (jugador 1) a un punto con 5 del rival (punto 6, índice 5)
        with self.assertRaises(ValueError):
            self.board.move_checker(0, 5)

if __name__ == '__main__':
    unittest.main()
