class Board:
    """
    Representa el tablero de Backgammon con 24 puntos.
    Cada punto puede tener fichas de un jugador.
    """

    def __init__(self):
        self.__points__ = [0] * 24
        self.__bar__ = {1: 0, -1: 0}  # Fichas golpeadas por jugador
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
        print(f"Barra: Jugador 1 → {self.__bar__[1]} | Jugador 2 → {self.__bar__[-1]}")
    
    def get_points(self):
        """Devuelve el estado de los 24 puntos del tablero."""
        return self.__points__
    
    def get_bar(self):
        """Devuelve la cantidad de fichas en la barra para cada jugador."""
        return self.__bar__

    def move_checker(self, from_point: int, to_point: int):
        """
        Mueve una ficha de un punto a otro.
        Si golpea una ficha enemiga, la envía a la barra.
        """
        if from_point < 0 or from_point > 23 or to_point < 0 or to_point > 23:
            raise ValueError("Los puntos deben estar entre 0 y 23")

        if self.__points__[from_point] == 0:
            raise ValueError(f"No hay fichas en el punto {from_point + 1}")

        # Determinar jugador que mueve
        owner = 1 if self.__points__[from_point] > 0 else -1

        # Reducir en origen
        self.__points__[from_point] -= owner

        # Caso: destino vacío o del mismo jugador
        if self.__points__[to_point] == 0 or (self.__points__[to_point] * owner > 0):
            self.__points__[to_point] += owner
        # Caso: destino con 1 ficha enemiga (la golpea)
        elif abs(self.__points__[to_point]) == 1 and (self.__points__[to_point] * owner < 0):
            hit_owner = 1 if self.__points__[to_point] > 0 else -1
            self.__bar__[hit_owner] += 1
            self.__points__[to_point] = owner
        else:
            # Movimiento inválido (bloqueado)
            self.__points__[from_point] += owner
            raise ValueError(f"Movimiento inválido de {from_point + 1} a {to_point + 1}")
        
    def can_move(self, from_point: int, to_point: int) -> bool:
        """Verifica si un movimiento es legal sin ejecutarlo."""
        if from_point < 0 or from_point > 23 or to_point < 0 or to_point > 23:
            return False

        if self.__points__[from_point] == 0:
            return False  # no hay fichas en origen

        owner = 1 if self.__points__[from_point] > 0 else -1

        # Caso: destino vacío o con fichas del mismo jugador
        if self.__points__[to_point] == 0 or (self.__points__[to_point] * owner > 0):
            return True

        # Caso: destino con 1 ficha enemiga (se puede golpear)
        if abs(self.__points__[to_point]) == 1 and (self.__points__[to_point] * owner < 0):
            return True

        # Caso: destino bloqueado (2 o más fichas enemigas)
        return False

    def reenter_from_bar(self, owner: int, entry_point: int):
        """
        Reintroduce una ficha desde la barra al tablero.
        owner: 1 para Jugador 1, -1 para Jugador 2.
        entry_point: índice donde intenta entrar (0-5 para J1, 18-23 para J2).
        """
        if self.__bar__[owner] == 0:
            raise ValueError("No hay fichas en la barra para este jugador.")

        if entry_point < 0 or entry_point > 23:
            raise ValueError("El punto de entrada debe estar entre 0 y 23.")

        # Verificar si el punto de entrada está bloqueado
        if self.__points__[entry_point] * owner < -1:
            raise ValueError("Punto de entrada bloqueado.")

        # Caso: golpea una ficha enemiga
        if self.__points__[entry_point] * owner == -1:
            hit_owner = 1 if self.__points__[entry_point] > 0 else -1
            self.__bar__[hit_owner] += 1
            self.__points__[entry_point] = owner
        else:
            # Entra normalmente
            self.__points__[entry_point] += owner

        # Restar de la barra
        self.__bar__[owner] -= 1
