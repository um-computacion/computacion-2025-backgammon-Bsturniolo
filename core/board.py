
from __future__ import annotations
from typing import List, Dict

class Board:
    """
    Tablero de Backgammon (24 puntos 0..23).
    points[i] > 0 -> fichas del J1; < 0 -> fichas del J2; 0 -> vacío.
    __bar__ guarda fichas golpeadas por jugador: {1: n, -1: n}.
    """

    def __init__(self):
        self.__points__: List[int] = [0] * 24
        self.__bar__: Dict[int, int] = {1: 0, -1: 0}
        self._setup_starting_position()

    def _setup_starting_position(self) -> None:
        self.__points__ = [0] * 24
        # J1
        self.__points__[0]  =  2
        self.__points__[11] =  5
        self.__points__[16] =  3
        self.__points__[18] =  5
        # J2
        self.__points__[23] = -2
        self.__points__[12] = -5
        self.__points__[7]  = -3
        self.__points__[5]  = -5
        self.__bar__ = {1: 0, -1: 0}

    # === Getters que devuelven REFERENCIA, no copia ===
    def get_points(self) -> List[int]:
        return self.__points__

    def get_bar(self) -> Dict[int, int]:
        return self.__bar__

    # === Utilidades internas ===
    def _owner_at(self, idx: int) -> int:
        v = self.__points__[idx]
        if v > 0: return 1
        if v < 0: return -1
        return 0

    def _is_blocked_for(self, owner: int, idx: int) -> bool:
        val = self.__points__[idx]
        return (val * owner) <= -2  # 2+ del rival

    # === Validación básica (sin dirección ni barra) ===
    def can_move(self, from_point: int, to_point: int) -> bool:
        if not (0 <= from_point <= 23 and 0 <= to_point <= 23):
            return False
        if self.__points__[from_point] == 0:
            return False
        owner = self._owner_at(from_point)
        if owner == 0:
            return False
        if self._is_blocked_for(owner, to_point):
            return False
        return True

    # === Mover (golpes/bloqueos) ===
    def move_checker(self, from_point: int, to_point: int) -> None:
        if not (0 <= from_point <= 23 and 0 <= to_point <= 23):
            raise ValueError("Los puntos deben estar entre 0 y 23")
        if self.__points__[from_point] == 0:
            raise ValueError(f"No hay fichas en el punto {from_point + 1}")

        owner = self._owner_at(from_point)
        if self._is_blocked_for(owner, to_point):
            raise ValueError("Movimiento inválido: destino bloqueado.")

        # sacar del origen
        self.__points__[from_point] -= owner
        dest_val = self.__points__[to_point]

        # golpe (exactamente 1 del rival)
        if dest_val * owner == -1:
            enemy = 1 if dest_val > 0 else -1
            self.__bar__[enemy] += 1
            self.__points__[to_point] = owner
        else:
            self.__points__[to_point] += owner

    # === Reingreso desde barra ===
    def reenter_from_bar(self, owner: int, entry_point: int) -> None:
        if owner not in (1, -1):
            raise ValueError("Owner inválido.")
        if self.__bar__.get(owner, 0) <= 0:
            raise ValueError("No hay fichas en la barra para reingresar.")
        if not (0 <= entry_point <= 23):
            raise ValueError("Los puntos deben estar entre 0 y 23")
        if self._is_blocked_for(owner, entry_point):
            raise ValueError("Punto de entrada bloqueado.")

        dest_val = self.__points__[entry_point]
        if dest_val * owner == -1:
            enemy = 1 if dest_val > 0 else -1
            self.__bar__[enemy] += 1
            self.__points__[entry_point] = owner
        else:
            self.__points__[entry_point] += owner

        self.__bar__[owner] -= 1
