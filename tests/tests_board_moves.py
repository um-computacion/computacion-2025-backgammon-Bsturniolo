import unittest
from core.board import Board

class TestBoardMoves(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_move_checker_valid(self):
        # Jugador 1 mueve una ficha del punto 1 (índice 0) al punto 2 (índice 1)
        self.board.move_checker(0, 1)
        puntos = self.board.get_points()
        self.assertEqual(puntos[0], 1)   # en el origen queda 1 ficha
        self.assertEqual(puntos[1], 1)   # en el destino aparece 1 ficha

    def test_move_checker_from_empty_point_raises(self):
        # Punto 4 (índice 3) arranca vacío → debe fallar
        with self.assertRaises(ValueError):
            self.board.move_checker(3, 4)

    def test_move_checker_blocked_point_raises(self):
        # Jugador 1 intenta mover del punto 1 (índice 0) al punto 6 (índice 5)
        # Pero en el punto 6 ya hay 5 fichas del rival (Jugador 2)
        with self.assertRaises(ValueError):
            self.board.move_checker(0, 5)

    def test_move_checker_hits_single_opponent_checker(self):
        # Preparamos: ponemos 1 ficha enemiga en punto 2 (índice 1)
        self.board.get_points()[1] = -1
        # Movemos Jugador 1 desde punto 1 (índice 0) al punto 2
        self.board.move_checker(0, 1)
        puntos = self.board.get_points()
        self.assertEqual(puntos[0], 1)   # en el origen queda 1
        self.assertEqual(puntos[1], 1)   # en destino queda ficha del jugador 1

if __name__ == '__main__':
    unittest.main()
