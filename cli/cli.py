
from __future__ import annotations
from typing import List

from core.game import BackgammonGame


# ========= Helpers de UI =========

def _idx_from_input(txt: str) -> int:
    """
    Normaliza a índice interno 0..23 con una regla SIN ambigüedades:
      - 1..24  => se interpreta como índice HUMANO, devuelve n-1
      - 0      => índice interno 0 (para power users)
      - otro   => ValueError
    """
    n = int(txt)
    if 1 <= n <= 24:
        return n - 1
    if n == 0:
        return 0
    raise ValueError("El punto debe estar en 1..24 (humano) o 0 (interno).")


def _render_row(indices: List[int], pts: List[int]) -> str:
    """
    Fila formateada: idx | valor | símbolo
      + = fichas Jugador 1, - = Jugador -1, . = vacío
    """
    cells = []
    for i in indices:
        v = pts[i]
        sym = "+" if v > 0 else "-" if v < 0 else "."
        cells.append(f"{i:02d}:{sym}{abs(v):>2}")
    return "  ".join(cells)


def render_board(game: BackgammonGame) -> None:
    pts = game.get_points()
    bar = game.get_bar()
    # top: 23 .. 12
    top = list(range(23, 11, -1))
    # bottom: 0 .. 11
    bottom = list(range(0, 12, 1))

    print("\n" + "=" * 78)
    print("TABLERO (índices internos 0..23; ingresa puntos humanos 1..24)")
    print("-" * 78)
    print("Arriba  (24→13):")
    print(_render_row(top, pts))
    print("-" * 78)
    print("Abajo   (1→12):")
    print(_render_row(bottom, pts))
    print("-" * 78)
    print(f"Barra: J1={bar.get(1, 0)} | J2={bar.get(-1, 0)}")
    print("=" * 78)


def render_header(game: BackgammonGame) -> None:
    pl = game.current_player()
    name = getattr(pl, "_name", getattr(pl, "name", "Jugador"))
    pid = getattr(pl, "_id", getattr(pl, "id", 1))
    moves = game.get_available_moves()
    print(f"\nTurno de {name} (id={pid}) | Dados disponibles: {moves if moves else '—'}")


def print_help() -> None:
    print(
        """
Comandos:
  tirar
  mover <from> <to>        # ingresa puntos HUMANOS 1..24 (ej: mover 6 8)  |  0 solo admite índice interno 0
  reingresar <idx>         # idem: 1..24 humano (o 0 solo si sabés que es el índice interno)
  fin                      # fuerza cambio de turno (si ya usaste todo, es automático)
  ver                      # vuelve a imprimir el tablero
  ayuda
  salir
        """.strip()
    )


# ========= Loop principal =========

def main() -> None:
    print("=== Backgammon (CLI) ===")
    print_help()

    # Nombres por defecto (podés cambiarlos acá)
    game = BackgammonGame("Jugador 1", "Jugador 2")
    render_board(game)

    while True:
        try:
            render_header(game)
            cmd = input("> ").strip()

            if not cmd:
                continue

            parts = cmd.split()
            action = parts[0].lower()

            if action in ("salir", "exit", "quit"):
                print("Saliendo...")
                break

            elif action in ("ayuda", "help", "?"):
                print_help()

            elif action in ("ver", "board", "tablero"):
                render_board(game)

            elif action == "tirar":
                vals = game.roll_dice()
                print(f"Dados: {vals}")

            elif action == "mover":
                if len(parts) != 3:
                    print("Uso: mover <from> <to>  (usa 1..24 humano)")
                    continue
                from_p = _idx_from_input(parts[1])
                to_p = _idx_from_input(parts[2])
                game.move(from_p, to_p)
                print(f"OK: moviste de {from_p}→{to_p}")
                render_board(game)

            elif action in ("reingresar", "reingreso", "entrar"):
                if len(parts) != 2:
                    print("Uso: reingresar <idx>  (usa 1..24 humano)")
                    continue
                idx = _idx_from_input(parts[1])
                game.reenter(idx)
                print(f"OK: reingresaste en {idx}")
                render_board(game)

            elif action == "fin":
                game.change_turn()
                print("Turno cambiado.")
                render_board(game)

            else:
                print("Comando no reconocido. Escribí 'ayuda' para ver opciones.")

        except Exception as e:
            print(f"Error: {e}")

    print("Gracias por jugar 🙂")


if __name__ == "__main__":  # pragma: no cover
    main()
