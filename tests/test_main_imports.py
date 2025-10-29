
import importlib
import pytest
from cli import cli

def test_import_cli_main_ok():
    m = importlib.import_module("cli.cli")
    assert hasattr(m, "main")

def test_import_pygame_main_ok():
    # Solo verifica que el módulo existe y expone 'run' (no lo ejecuta).
    m = importlib.import_module("pygame_ui.main")
    assert hasattr(m, "run")

def test_idx_from_input_valid_and_invalid():
    # Regla nueva: 1..24 (humano) -> 0..23 (interno); 0 -> 0 interno
    assert cli._idx_from_input("1") == 0
    assert cli._idx_from_input("24") == 23
    assert cli._idx_from_input("0") == 0
    # Fuera de rango
    with pytest.raises(ValueError):
        cli._idx_from_input("25")
