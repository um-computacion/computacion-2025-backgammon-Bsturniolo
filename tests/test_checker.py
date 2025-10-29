import unittest
from core.checker import checker

class TestChecker(unittest.TestCase):

    def test_checker_has_owner(self):
        ficha = checker(1)
        self.assertEqual(ficha.get_owner(), 1)

    def test_checker_repr(self):
        ficha = checker(-1)
        self.assertEqual(repr(ficha), "checker(-1)")

if __name__ == "__main__":
    unittest.main()
