import unittest
from core.game import BackgammonGame

class TestGameMoves(unittest.TestCase):
    """Pruebas para los movimientos del juego Backgammon."""

    def setUp(self):
        """Configura una partida nueva antes de cada test."""
        self.game = BackgammonGame()
        self.board = self.game.get_board()

    def test_roll_dice_creates_available_moves(self):
        """Verifica que al tirar los dados se generen movimientos disponibles."""
        moves = self.game.roll_dice()
        self.assertTrue(len(moves) in [2, 4])  # dos normales o cuatro si hay dobles
        self.assertEqual(self.game.get_available_moves(), moves)

    def test_move_uses_die_value(self):
        """Verifica que un movimiento consuma un valor de dado."""
        # Forzamos un resultado de dados predecible
        self.game.__available_moves__ = [3, 5]

        from_point, to_point = 0, 3  # mueve 3 puntos
        self.board.get_points()[from_point] = 2
        self.board.get_points()[to_point] = 0

        self.game.move(from_point, to_point)

        # Después del movimiento, el dado 3 debería consumirse
        self.assertNotIn(3, self.game.get_available_moves())

    def test_invalid_move_distance(self):
        """Verifica que un movimiento con distancia no válida lanza error."""
        self.game.__available_moves__ = [3, 5]

        with self.assertRaises(ValueError):
            self.game.move(0, 4)  # distancia 4 no está en los dados

    def test_cannot_move_without_dice(self):
        """No se puede mover si no se lanzaron los dados."""
        with self.assertRaises(ValueError):
            self.game.move(0, 1)

    def test_turn_changes_when_no_moves_left(self):
        """El turno cambia automáticamente cuando no quedan movimientos."""
        self.game.__available_moves__ = [2]
        self.board.get_points()[0] = 1
        self.board.get_points()[2] = 0

        current_player_before = self.game.current_player()
        self.game.move(0, 2)
        current_player_after = self.game.current_player()

        # Verificamos que cambió el turno
        self.assertNotEqual(current_player_before, current_player_after)

if __name__ == '__main__':
    unittest.main()
