class Player:
    """
    Representa a un jugador de Backgammon.
    """

    def __init__(self, name: str, id_: int):
        """
        name: nombre del jugador
        id_: 1 para jugador 1, -1 para jugador 2
        """
        self._name = name
        self._id = id_
        self._checkers = []      # fichas del jugador
        self._bar = []           # fichas capturadas (en la barra)
        self._borne_off = []     # fichas que ya salieron del tablero

    def __repr__(self):
        return f"Player({self._name}, id={self._id})"
