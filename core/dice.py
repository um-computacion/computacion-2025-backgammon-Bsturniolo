import random

class Dice:
    """
    Representa dos dados de Backgammon.
    """

    def __init__(self):
        self.__values__ = []

    def roll(self):
        """Lanza los dados y guarda el resultado."""
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)

        # Si es doble, se repite el valor 4 veces
        if d1 == d2:
            self.__values__ = [d1] * 4
        else:
            self.__values__ = [d1, d2]

        return self.__values__

    def get_values(self):
        """Devuelve los valores actuales de los dados."""
        return self.__values__
