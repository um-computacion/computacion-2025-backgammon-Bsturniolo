
import builtins
import pytest
from cli import cli

def run_cli_with_inputs(seq):
    it = iter(seq)
    def fake_input(_="> "):
        try:
            return next(it)
        except StopIteration:
            return "salir"
    # parchear input
    return fake_input

def test_cli_unknown_command(monkeypatch, capsys):
    # Cubre rama "comando no reconocido" (142–145)
    monkeypatch.setattr("builtins.input", run_cli_with_inputs(["foobar", "salir"]))
    cli.main()
    out = capsys.readouterr().out
    assert "Comando no reconocido" in out

def test_cli_mover_argumentos_invalidos(monkeypatch, capsys):
    # Cubre rama "Uso: mover <from> <to>" (119–120)
    monkeypatch.setattr("builtins.input", run_cli_with_inputs(["mover 5", "salir"]))
    cli.main()
    out = capsys.readouterr().out
    assert "Uso: mover <from> <to>" in out

def test_cli_reingresar_argumentos_invalidos(monkeypatch, capsys):
    # Cubre rama "Uso: reingresar <idx>" (129–130)
    monkeypatch.setattr("builtins.input", run_cli_with_inputs(["reingresar", "salir"]))
    cli.main()
    out = capsys.readouterr().out
    assert "Uso: reingresar <idx>" in out
