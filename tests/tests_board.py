import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def test_board_has_24_points(self):
        board = Board()
        self.assertEqual(len(board.get_points()), 24)

    def test_starting_position_player1(self):
        board = Board()
        # Jugador 1 empieza con:
        self.assertEqual(board.get_points()[0], 2)    # 2 fichas en punto 1
        self.assertEqual(board.get_points()[11], 5)   # 5 fichas en punto 12
        self.assertEqual(board.get_points()[16], 3)   # 3 fichas en punto 17
        self.assertEqual(board.get_points()[18], 5)   # 5 fichas en punto 19

    def test_starting_position_player2(self):
        board = Board()
        # Jugador 2 empieza con:
        self.assertEqual(board.get_points()[23], -2)  # 2 fichas en punto 24
        self.assertEqual(board.get_points()[12], -5)  # 5 fichas en punto 13
        self.assertEqual(board.get_points()[7], -3)   # 3 fichas en punto 8
        self.assertEqual(board.get_points()[5], -5)   # 5 fichas en punto 6

    # 🚀 Nuevos tests para can_move
    def test_can_move_valid(self):
        board = Board()
        self.assertTrue(board.can_move(0, 1))  # Jugador 1 del punto 1 al 2

    def test_can_move_from_empty_point(self):
        board = Board()
        self.assertFalse(board.can_move(3, 4))  # Punto 4 arranca vacío

    def test_can_move_blocked_point(self):
        board = Board()
        # Jugador 1 intenta del punto 1 (índice 0) al punto 6 (índice 5) → bloqueado
        self.assertFalse(board.can_move(0, 5))

    def test_can_move_hit_single_checker(self):
        board = Board()
        # Preparar: poner una ficha enemiga en el punto 2 (índice 1)
        board.get_points()[1] = -1
        self.assertTrue(board.can_move(0, 1))  # Puede golpear

if __name__ == '__main__':
    unittest.main()
