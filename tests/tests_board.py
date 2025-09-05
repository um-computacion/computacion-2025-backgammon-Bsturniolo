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

if __name__ == '__main__':
    unittest.main()
