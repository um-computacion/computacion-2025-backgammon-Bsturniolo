
from __future__ import annotations
from typing import List, Optional

from core.board import Board
from core.dice import Dice
from core.player import Player

__all__ = ["BackgammonGame"]

def _make_player(name: str, id_value: int) -> Player:
    """Tolera Player(name, id_=...), Player(name, id=...), Player(name, ...)"""
    try:
        return Player(name, id_=id_value)
    except TypeError:
        try:
            return Player(name, id=id_value)
        except TypeError:
            return Player(name, id_value)

class BackgammonGame:
    def __init__(self, player1_name: str = "Jugador 1", player2_name: str = "Jugador 2"):
        self.__board__ = Board()
        # Mantengo TRES punteros al mismo objeto para máxima compatibilidad
        base_dice = Dice()
        self.__dice__ = base_dice                 # para tests que usan _BackgammonGame__dice__
        self.dice = base_dice                     # para inyección pública: game.dice = DummyDice(...)
        self.__players__ = [_make_player(player1_name, 1), _make_player(player2_name, -1)]
        self.__current_idx__ = 0
        self.__available_moves__: List[int] = []

    # ----- Helpers / getters usados por tests -----
    def get_board(self) -> Board:
        return self.__board__

    def get_points(self) -> List[int]:
        return self.__board__.get_points()

    def get_bar(self) -> dict:
        return self.__board__.get_bar()

    def current_player(self):
        return self.__players__[self.__current_idx__]

    def get_available_moves(self) -> List[int]:
        return list(self.__available_moves__)

    # ----- Setter de dado (opcional) -----
    def set_dice(self, dice: Dice) -> None:
        """Inyecta un dado determinístico para tests (sin pelear con name-mangling)."""
        self.__dice__ = dice
        self.dice = dice

    # ----- Dados y turnos -----
    def _resolve_dice(self) -> Dice:
        """
        Devuelve el objeto 'dado' a usar, priorizando:
          1) atributo privado _BackgammonGame__dice__ (si el test lo setea)
          2) atributo público 'dice'
          3) atributo privado __dice__ (fallback)
        """
        # 1) Si el test setea directamente el atributo mangled:
        injected = getattr(self, "_BackgammonGame__dice__", None)
        if injected is not None:
            return injected
        # 2) si usan atributo público
        if getattr(self, "dice", None) is not None:
            return self.dice
        # 3) fallback
        return self.__dice__

    def roll_dice(self) -> List[int]:
        """
        Lanza los dados del turno. Si es doble, el objeto Dice debe ya devolver
        [d,d,d,d]. NO duplicamos aquí.
        """
        dice_obj = self._resolve_dice()
        values = dice_obj.roll()
        self.__available_moves__ = list(values)
        return self.get_available_moves()

    def change_turn(self) -> None:
        self.__current_idx__ = 1 - self.__current_idx__
        self.__available_moves__.clear()

    # ----- Dirección -----
    @staticmethod
    def _is_forward(owner: int, from_point: int, to_point: int) -> bool:
        return (to_point > from_point) if owner == 1 else (to_point < from_point)

    # ----- Movimiento principal -----
    def move(self, from_point: int, to_point: int) -> None:
        if not self.__available_moves__:
            raise ValueError("No hay movimientos disponibles. Lanza los dados primero.")

        owner = getattr(self.current_player(), "_id", 1 if self.__current_idx__ == 0 else -1)

        # Barra primero
        if self.__board__.get_bar().get(owner, 0) > 0:
            raise ValueError("Tenés fichas en la barra: reingresá antes de mover otras.")

        # Dirección obligatoria
        if not self._is_forward(owner, from_point, to_point):
            raise ValueError(
                "Dirección inválida para Jugador 1 (debe avanzar a índices mayores)."
                if owner == 1 else
                "Dirección inválida para Jugador 2 (debe avanzar a índices menores)."
            )

        distance = abs(to_point - from_point)
        if distance not in self.__available_moves__:
            raise ValueError(f"Movimiento inválido. Los dados no permiten mover {distance} puntos.")

        if not self.__board__.can_move(from_point, to_point):
            raise ValueError("Movimiento no permitido por el tablero.")

        self.__board__.move_checker(from_point, to_point)

        self.__available_moves__.remove(distance)
        if not self.__available_moves__:
            self.change_turn()

    # ----- Reingreso desde barra -----
    def reenter(self, entry_point: int) -> None:
        owner = getattr(self.current_player(), "_id", 1 if self.__current_idx__ == 0 else -1)
        if self.__board__.get_bar().get(owner, 0) <= 0:
            raise ValueError("No tenés fichas en la barra para reingresar.")

        # Distancia simplificada compatible con tests:
        # J1 entra por 0..5 → distancia = entry_point + 1
        # J2 entra por 23..18 → distancia = 24 - entry_point
        distance = (entry_point + 1) if owner == 1 else (24 - entry_point)
        if distance not in self.__available_moves__:
            raise ValueError("El valor de dado no permite reingresar en ese punto.")

        self.__board__.reenter_from_bar(owner, entry_point)

        self.__available_moves__.remove(distance)
        if not self.__available_moves__:
            self.change_turn()

    def is_game_over(self) -> Optional[int]:
        return None
