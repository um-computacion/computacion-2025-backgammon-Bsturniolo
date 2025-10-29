# tests/conftest.py
import sys
from pathlib import Path

# Ruta raíz del repo (carpeta que contiene 'core', 'tests', etc.)
ROOT = Path(__file__).resolve().parents[1]
ROOT_STR = str(ROOT)

# Asegura que 'core' sea importable como 'core.*' sin depender del cwd
if ROOT_STR not in sys.path:
    sys.path.insert(0, ROOT_STR)
