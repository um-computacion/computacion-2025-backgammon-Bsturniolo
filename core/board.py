class Board:
    """
    Representa el tablero de Backgammon con 24 puntos.
    Cada punto puede tener fichas de un jugador.
    """

    def __init__(self):
        self.__points__ = [0] * 24
        self._setup_starting_position()

    def _setup_starting_position(self):
        """Configura la posición inicial de las fichas en el tablero."""
        # Jugador 1 (positivo)
        self.__points__[0] = 2
        self.__points__[11] = 5
        self.__points__[16] = 3
        self.__points__[18] = 5

        # Jugador 2 (negativo)
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
    
    def get_points(self):
        """Devuelve el estado de los 24 puntos del tablero."""
        return self.__points__

    def move_checker(self, from_point: int, to_point: int):
        """
        Mueve una ficha de un punto a otro.
        
        from_point y to_point son índices (0-23).
        """
        if from_point < 0 or from_point > 23 or to_point < 0 or to_point > 23:
            raise ValueError("Los puntos deben estar entre 0 y 23")

        if self.__points__[from_point] == 0:
            raise ValueError(f"No hay fichas en el punto {from_point + 1}")

        # Determinar jugador que mueve
        owner = 1 if self.__points__[from_point] > 0 else -1

        # Reducir en origen
        self.__points__[from_point] -= owner

        # Si el destino tiene fichas del mismo jugador o está vacío
        if self.__points__[to_point] == 0 or (self.__points__[to_point] * owner > 0):
            self.__points__[to_point] += owner
        # Si el destino tiene solo 1 ficha enemiga → la "golpea"
        elif abs(self.__points__[to_point]) == 1 and (self.__points__[to_point] * owner < 0):
            # TODO: enviar la ficha golpeada a la barra
            self.__points__[to_point] = owner
        else:
            # Movimiento inválido (bloqueado)
            # Revertimos origen
            self.__points__[from_point] += owner
            raise ValueError(f"Movimiento inválido de {from_point + 1} a {to_point + 1}")
