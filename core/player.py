class Player:
    """
    Representa a un jugador de Backgammon.
    """

    def __init__(self, name: str, id_: int):
        """
        name: nombre del jugador
        id_: 1 para jugador 1, -1 para jugador 2
        """
        self.__name__ = name
        self.__id__ = id_
        self.__checkers__ = []      # fichas del jugador
        self.__bar__ = []           # fichas capturadas (en la barra)
        self.__borne_off__ = []     # fichas que ya salieron del tablero

    def __repr__(self):
        return f"Player({self.__name__}, id={self.__id__})"
