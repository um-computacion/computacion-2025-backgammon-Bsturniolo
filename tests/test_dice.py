import unittest
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_roll_returns_values_between_1_and_6(self):
        dice = Dice()
        values = dice.roll()
        for v in values:
            self.assertGreaterEqual(v, 1)
            self.assertLessEqual(v, 6)

    def test_roll_double_results_in_four_values(self):
        dice = Dice()
        # Intentar varias veces hasta que salga un doble real
        for _ in range(100):  # 100 intentos como máximo
            values = dice.roll()
            if len(values) == 4:  # si salió doble
                self.assertEqual(len(values), 4)
                return
        self.fail("No se generó un doble en 100 intentos")

    def test_get_values_returns_last_roll(self):
        dice = Dice()
        result = dice.roll()
        self.assertEqual(dice.get_values(), result)

if __name__ == '__main__':
    unittest.main()
