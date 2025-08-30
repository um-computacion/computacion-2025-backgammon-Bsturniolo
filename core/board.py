class Board:
    """
    Representa el tablero de Backgammon con 24 puntos.
    Cada punto puede tener fichas de un jugador.
    """

    def __init__(self):
        self.__points__ = [0] * 24
        self._setup_starting_position()

    def _setup_starting_position(self):
        self.__points__[0] = 2
        self.__points__[11] = 5
        self.__points__[16] = 3
        self.__points__[18] = 5

        self.__points__[23] = -2
        self.__points__[12] = -5
        self.__points__[7] = -3
        self.__points__[5] = -5

    def show(self):
        """Muestra el tablero en consola de forma legible."""
        print("\n=== Tablero ===")
        for i, val in enumerate(self.__points__, start=1):
            print(f"Punto {i:2}: {val}")
        print("================\n")
