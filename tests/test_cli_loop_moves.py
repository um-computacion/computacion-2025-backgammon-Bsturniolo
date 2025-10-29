
import types
import builtins
import pytest
from cli import cli

class DummyPlayer:
    def __init__(self, name, pid):
        self._name = name
        self._id = pid

class DummyGame:
    """Falso BackgammonGame para testear la CLI sin lógica real."""
    def __init__(self, *a, **k):
        self._moves = []
        self._bar = {1: 0, -1: 0}
        self._points = [0]*24
        self._current = DummyPlayer("Dummy", 1)
        self._available = []

    # usados por render
    def get_points(self): return self._points
    def get_bar(self): return self._bar
    def current_player(self): return self._current
    def get_available_moves(self): return list(self._available)

    # comandos
    def roll_dice(self):
        self._available = [2]   # valor determinístico
        return list(self._available)

    def move(self, from_p, to_p):
        # No validamos nada; solo registramos para cubrir ramas
        self._moves.append(("move", from_p, to_p))
        if 2 in self._available:
            self._available.remove(2)

    def reenter(self, idx):
        self._moves.append(("reenter", idx))
        # no cambia nada; alcanza para cubrir rama CLI

    def change_turn(self):
        self._moves.append(("turn",))

def test_cli_main_simulated_session(monkeypatch, capsys):
    """
    Simula una sesión CLI:
      ayuda → tirar → mover 1 3 → reingresar 1 → fin → salir
    """
    # Parcheamos la clase BackgammonGame dentro del módulo cli
    monkeypatch.setattr(cli, "BackgammonGame", DummyGame)

    inputs = iter(["ayuda", "tirar", "mover 1 3", "reingresar 1", "fin", "salir"])

    def fake_input(_="> "):
        try:
            return next(inputs)
        except StopIteration:
            return "salir"

    monkeypatch.setattr(builtins, "input", fake_input)

    # Ejecutamos main()
    cli.main()

    out = capsys.readouterr().out
    # Verificamos que pasaron por varias ramas
    assert "Comandos" in out            # ayuda
    assert "Dados:" in out              # tirar
    assert "moviste" in out or "OK:" in out or "Reingreso" in out or "Turno cambiado." in out
