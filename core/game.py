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

    def roll_dice(self):
        """Lanza los dados y devuelve los valores."""
        return self.__dice__.roll()

    def show_board(self):
        """Muestra el tablero en consola."""
        self.__board__.show()

    def change_turn(self):
        """Cambia al otro jugador."""
        self.__turn__ = 1 - self.__turn__

    def current_player(self):
        """Devuelve el jugador actual."""
        return self.__players__[self.__turn__]
