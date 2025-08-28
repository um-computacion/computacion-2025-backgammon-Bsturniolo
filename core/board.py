class Board:
    """
    Representa el tablero de Backgammon con 24 puntos.
    Cada punto puede tener fichas de un jugador.
    """

    def __init__(self):
        # 24 puntos, cada índice = posición en el tablero
        # positivo = jugador 1, negativo = jugador 2
        self.__points__ = [0] * 24
        self._setup_starting_position()

    def _setup_starting_position(self):
        """Configura la posición inicial estándar del Backgammon."""
        self.__points__[0] = 2      # Jugador 1: 2 fichas en punto 1
        self.__points__[11] = 5     # Jugador 1: 5 fichas en punto 12
        self.__points__[16] = 3     # Jugador 1: 3 fichas en punto 17
        self.__points__[18] = 5     # Jugador 1: 5 fichas en punto 19

        self.__points__[23] = -2    # Jugador 2: 2 fichas en punto 24
        self.__points__[12] = -5    # Jugador 2: 5 fichas en punto 13
        self.__points__[7] = -3     # Jugador 2: 3 fichas en punto 8
        self.__points__[5] = -5     # Jugador 2: 5 fichas en punto 6

    def show(self):
        """Muestra el tablero en su estado actual (modo texto)."""
        print("Tablero:", self.__points__)
