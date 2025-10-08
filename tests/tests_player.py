import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_creation(self):
        player = Player("Jugador 1", 1)
        self.assertEqual(player._name, "Jugador 1")
        self.assertEqual(player._id, 1)
        self.assertEqual(player._checkers, [])
        self.assertEqual(player._bar, [])
        self.assertEqual(player._borne_off, [])

    def test_add_checker_to_board(self):
        player = Player("Jugador 1", 1)
        player._checkers.append("Ficha1")
        self.assertIn("Ficha1", player._checkers)

    def test_capture_checker(self):
        player = Player("Jugador 1", 1)
        player._bar.append("FichaRival")
        self.assertIn("FichaRival", player._bar)

    def test_bear_off_checker(self):
        player = Player("Jugador 1", 1)
        player._borne_off.append("Ficha1")
        self.assertIn("Ficha1", player._borne_off)
