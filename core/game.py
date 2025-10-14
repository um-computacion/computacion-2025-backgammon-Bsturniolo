from core.board import Board
from core.dice import Dice
from core.player import Player

class BackgammonGame:
    """
    Clase principal que coordina el flujo del Backgammon.
    """

    def __init__(self, player1_name="Jugador 1", player2_name="Jugador 2"):
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__players__ = [
            Player(player1_name, id_=1),
            Player(player2_name, id_=-1)
        ]
        self.__turn__ = 0  # índice del jugador actual (0 o 1)
        self.__available_moves__ = []  # movimientos posibles según los dados

    def roll_dice(self):
        """Lanza los dados y guarda los valores disponibles."""
        values = self.__dice__.roll()
        # Si es doble, hay 4 movimientos iguales
        self.__available_moves__ = values * 2 if values[0] == values[1] else values
        return self.__available_moves__

    def get_board(self):
        """Devuelve el tablero."""
        return self.__board__

    def show_board(self):
        """Muestra el tablero en consola."""
        self.__board__.show()

    def change_turn(self):
        """Cambia al otro jugador."""
        self.__turn__ = 1 - self.__turn__
        self.__available_moves__ = []  # reinicia los dados al cambiar turno

    def current_player(self):
        """Devuelve el jugador actual."""
        return self.__players__[self.__turn__]

    def get_available_moves(self):
        """Devuelve los movimientos aún disponibles en este turno."""
        return self.__available_moves__

    def move(self, from_point: int, to_point: int):
        """
        Realiza un movimiento del punto origen al destino,
        usando uno de los valores de los dados.
        """
        if not self.__available_moves__:
            raise ValueError("No hay movimientos disponibles. Lanza los dados primero.")

        distance = abs(to_point - from_point)
        if distance not in self.__available_moves__:
            raise ValueError(f"Movimiento inválido. Los dados no permiten mover {distance} puntos.")

        board = self.__board__
        player = self.current_player()
        owner = player._id  # usa el id interno del jugador

        # Validar movimiento en el tablero
        if not board.can_move(from_point, to_point):
            raise ValueError("Movimiento no permitido por el tablero.")

        # Ejecutar el movimiento
        board.move_checker(from_point, to_point)

        # Remover el valor usado del dado
        self.__available_moves__.remove(distance)

        print(f"{player._name} movió una ficha de {from_point + 1} a {to_point + 1} usando el dado {distance}.")

        # Si no quedan movimientos → cambiar turno automáticamente
        if not self.__available_moves__:
            print("Turno completado. Cambiando jugador...")
            self.change_turn()
