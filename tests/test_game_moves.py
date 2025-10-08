import unittest
from core.game import BackgammonGame

class TestGameMoves(unittest.TestCase):

    def setUp(self):
        self.game = BackgammonGame()
        self.board = self.game.get_board()

    def test_roll_dice_creates_available_moves(self):
        """Verifica que al lanzar los dados se guarden movimientos disponibles."""
        moves = self.game.roll_dice()
        self.assertTrue(len(moves) in [2, 4])  # 2 normales o 4 si es doble
        self.assertEqual(self.game.get_available_moves(), moves)

    def test_move_uses_dice_value(self):
        """Verifica que un movimiento válido consume el valor del dado."""
        self.game._BackgammonGame__available_moves__ = [3, 4]  # simular tirada
        self.board.get_points()[0] = 1
        self.board.get_points()[3] = 0

        self.game.move(0, 3)
        self.assertNotIn(3, self.game.get_available_moves())

    def test_invalid_move_not_in_dice_values(self):
        """Verifica que no se pueda mover si la distancia no coincide con un dado."""
        self.game._BackgammonGame__available_moves__ = [3, 5]
        with self.assertRaises(ValueError):
            self.game.move(0, 1)  # distancia 1 no está en los dados

    def test_invalid_move_blocked_point(self):
        """Verifica que no se pueda mover a un punto bloqueado."""
        self.game._BackgammonGame__available_moves__ = [3]
        self.board.get_points()[0] = 1
        self.board.get_points()[3] = -2  # bloqueado
        with self.assertRaises(ValueError):
            self.game.move(0, 3)

    def test_turn_changes_when_no_moves_left(self):
        """El turno debe cambiar automáticamente cuando no quedan movimientos."""
        self.game._BackgammonGame__available_moves__ = [2]
        self.board.get_points()[0] = 1
        self.board.get_points()[2] = 0
        current_player = self.game.current_player()
        self.game.move(0, 2)
        self.assertNotEqual(self.game.current_player(), current_player)

if __name__ == "__main__":
    unittest.main()
