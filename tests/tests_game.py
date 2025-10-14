import unittest
from core.game import BackgammonGame

class TestBackgammonGame(unittest.TestCase):

    def setUp(self):
        # Creamos un juego nuevo con jugadores personalizados
        self.game = BackgammonGame("Alice", "Bob")

    def test_initial_player(self):
        """Verifica que el primer jugador sea el correcto."""
        jugador = self.game.current_player()
        self.assertEqual(jugador._name, "Alice")
        self.assertEqual(jugador._id, 1)

    def test_change_turn(self):
        """Verifica que el turno cambia correctamente."""
        jugador_inicial = self.game.current_player()
        self.game.change_turn()
        jugador_siguiente = self.game.current_player()
        self.assertNotEqual(jugador_inicial, jugador_siguiente)
        # Volvemos al primer jugador
        self.game.change_turn()
        self.assertEqual(self.game.current_player(), jugador_inicial)

    def test_roll_dice_values(self):
        """Verifica que los dados devuelvan valores válidos."""
        dados = self.game.roll_dice()
        self.assertTrue(all(1 <= d <= 6 for d in dados))
        self.assertIn(len(dados), [2, 4])  # normales o dobles

    def test_board_initial_setup(self):
        """Verifica la configuración inicial del tablero."""
        puntos = self.game.get_board().get_points()  # usamos getter
        self.assertEqual(puntos[0], 2)
        self.assertEqual(puntos[23], -2)
        self.assertEqual(puntos[11], 5)
        self.assertEqual(puntos[12], -5)
        self.assertEqual(puntos[16], 3)
        self.assertEqual(puntos[18], 5)
        self.assertEqual(puntos[5], -5)
        self.assertEqual(puntos[7], -3)

if __name__ == "__main__":
    unittest.main()
