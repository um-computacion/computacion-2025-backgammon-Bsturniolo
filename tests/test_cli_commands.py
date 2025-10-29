
import pytest
from cli import cli
from core.game import BackgammonGame


# ---------- Tests unitarios de funciones auxiliares ----------

def test_idx_from_input_valid_and_invalid():
    # Entradas válidas con la NUEVA REGLA:
    # humano 1..24 => 0..23 ; 0 => 0 interno
    assert cli._idx_from_input("1") == 0
    assert cli._idx_from_input("24") == 23
    assert cli._idx_from_input("0") == 0
    # inválido
    with pytest.raises(ValueError):
        cli._idx_from_input("25")


def test_render_board_and_header(capsys):
    g = BackgammonGame()
    cli.render_board(g)
    cli.render_header(g)
    out = capsys.readouterr().out
    assert "TABLERO" in out
    assert "Barra" in out


def test_print_help_output(capsys):
    cli.print_help()
    out = capsys.readouterr().out
    assert "Comandos" in out


# ---------- Simulación del loop principal (sin interacción real) ----------

def test_main_loop_simulated(monkeypatch, capsys):
    """
    Simula una sesión corta del main():
      - 'ayuda' -> 'tirar' -> 'ver' -> 'fin' -> 'salir'
    Verifica que el loop corre sin error y emite salida.
    """
    inputs = iter(["ayuda", "tirar", "ver", "fin", "salir"])

    def fake_input(_prompt="> "):
        try:
            return next(inputs)
        except StopIteration:
            return "salir"

    monkeypatch.setattr("builtins.input", fake_input)
    cli.main()
    out = capsys.readouterr().out
    assert "Comandos" in out
    assert "TABLERO" in out or "Turno" in out
