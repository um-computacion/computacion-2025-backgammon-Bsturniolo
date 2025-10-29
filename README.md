# 🎲 Backgammon Computación 2025

> Proyecto académico desarrollado en **Python 3.11** como parte de la cátedra de **Computación**.  
> Implementa el clásico juego **Backgammon** con interfaz por consola (CLI) y una versión visual en **Pygame**, incluyendo una suite completa de **tests automatizados**.

---

## 🧠 Descripción general

**Backgammon Computación 2025** es una recreación modular del juego de mesa Backgammon, enfocada en la correcta aplicación de diseño, encapsulamiento, testing y cobertura de código.  
El sistema permite jugar partidas completas con lógica de movimientos, barra, reingresos y turnos, y puede ejecutarse tanto desde la consola como desde una interfaz visual.

### 🎮 Módulos principales

| Carpeta | Descripción |
|----------|--------------|
| `core/` | Contiene la lógica central del juego: tablero (`Board`), fichas (`Checker`), dados (`Dice`), jugadores (`Player`) y control general (`BackgammonGame`). |
| `cli/` | Interfaz de texto. Permite jugar mediante comandos simples en la terminal (`tirar`, `mover`, `reingresar`, etc.). |
| `pygame_ui/` | Interfaz gráfica realizada con **Pygame**, que muestra el tablero y permite mover fichas con el mouse. |
| `tests/` | Conjunto de pruebas unitarias escritas con **Pytest** para verificar el comportamiento de cada módulo. |
| `.github/workflows/` | Contiene el workflow de **GitHub Actions** para ejecutar los tests automáticamente al realizar un push. |

---

## ⚙️ Estructura del proyecto

Backgammon/
│
├── core/
│ ├── board.py
│ ├── game.py
│ ├── player.py
│ ├── checker.py
│ └── dice.py
│
├── cli/
│ └── cli.py
│
├── pygame_ui/
│ └── main.py
│
├── tests/
│ ├── test_board.py
│ ├── test_game.py
│ ├── test_cli_commands.py
│ ├── ...
│ └── test_game_more_edges.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .github/workflows/tests.yml

## 🚀 Ejecución

### ▶️ Desde la consola (CLI)
```bash
python -m cli.cli

🕹️ Desde la interfaz gráfica (Pygame)

python -m pygame_ui.main

🎯 Comandos disponibles (CLI)

| Comando                    | Descripción                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `tirar`                    | Lanza los dados del turno actual.                                |
| `mover <origen> <destino>` | Mueve una ficha entre puntos (usar 1–24 como numeración humana). |
| `reingresar <punto>`       | Reingresa una ficha desde la barra.                              |
| `fin`                      | Cambia manualmente el turno.                                     |
| `ver`                      | Muestra nuevamente el tablero.                                   |
| `ayuda`                    | Lista todos los comandos.                                        |
| `salir`                    | Finaliza la partida.                                             |

🧪 Testing y Cobertura

El proyecto utiliza Pytest + Coverage.py para garantizar calidad de código y correcto funcionamiento.

python -m pytest --cov --cov-report=term-missing

📊 Resultados finales
Métrica	Valor
Tests ejecutados	59
Tests exitosos	100 %
Cobertura total	89 %
Módulos clave	core/board.py 96 %, core/game.py 78 %, cli/cli.py 90 %

🧩 Se alcanzó el umbral de cobertura mínimo exigido (85 %) y se superó ampliamente.

🧰 Requisitos

Python ≥ 3.10
Librerías del archivo requirements.txt
pip install -r requirements.txt

✅ Integración continua
Este proyecto cuenta con un pipeline automatizado que ejecuta los tests al hacer push o pull request sobre main.

# .github/workflows/tests.yml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: |
          pip install -r requirements.txt
          python -m pytest -q --cov

🏁 Conclusión

Este trabajo implementa de forma completa la lógica del juego Backgammon, cumpliendo con:
Modularidad, encapsulamiento y uso de patrones básicos.
Testing exhaustivo con más de 59 pruebas unitarias.
Cobertura superior al 85 % y validación automática en CI.
Interfaz dual: CLI + Gráfica en Pygame.
Desarrollado por Bautista Sturniolo – Universidad de Mendoza ( Materia computación 2025 ).
🧠 “El código es el tablero; las pruebas son la estrategia.”