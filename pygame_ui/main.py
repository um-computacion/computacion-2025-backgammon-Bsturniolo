# pygame_ui/main.py
from __future__ import annotations
import sys
import pygame as pg

# Importa tu lógica del juego
from core.game import BackgammonGame

# ========= Config visual =========
W, H = 1024, 640
MARGIN = 20
BOARD_W = W - 2 * MARGIN
BOARD_H = H - 2 * MARGIN
MID_GAP = 80  # ancho de la "barra" central
COLS = 12
POINT_W = (BOARD_W - MID_GAP) // COLS // 2 * 2  # par
POINT_H = (BOARD_H - 60) // 2
CHECKER_R = min(POINT_W // 3, 18)
FONT_NAME = None

# Colores
BG = (35, 35, 38)
BOARD_BG = (210, 180, 140)   # madera clara
TRI_DARK = (150, 75, 0)
TRI_LIGHT = (230, 200, 150)
WHITE = (245, 245, 245)
BLACK = (0, 0, 0)
RED = (198, 54, 54)          # J2 (negativo)
BLUE = (54, 120, 198)        # J1 (positivo)
HUD = (235, 235, 240)
HUD_TEXT = (30, 30, 35)
ERR = (255, 120, 120)
OK = (120, 220, 140)

# ========= Mapeo de índices =========

def index_to_screen_pos(idx: int, is_top: bool) -> pg.Rect:
    """Rect base donde apilar fichas para un punto."""
    if is_top:
        col = 23 - idx      # 23..12 -> 0..11
    else:
        col = idx           # 0..11   -> 0..11

    if col < 6:
        x = MARGIN + col * (POINT_W)
    else:
        x = MARGIN + col * (POINT_W) + MID_GAP

    y = MARGIN if is_top else (H - MARGIN - POINT_H)
    return pg.Rect(int(x), int(y), int(POINT_W), int(POINT_H))

def point_is_top(idx: int) -> bool:
    return 12 <= idx <= 23

def iter_points_top():
    for idx in range(23, 11, -1):
        yield idx

def iter_points_bottom():
    for idx in range(0, 12):
        yield idx

# ========= Dibujo =========
def draw_board(surface: pg.Surface):
    surface.fill(BG)
    board_rect = pg.Rect(MARGIN, MARGIN, BOARD_W, BOARD_H)
    pg.draw.rect(surface, BOARD_BG, board_rect, border_radius=12)

    # Triángulos (arriba)
    for j, idx in enumerate(iter_points_top()):
        r = index_to_screen_pos(idx, True)
        color = TRI_DARK if j % 2 == 0 else TRI_LIGHT
        pts = [(r.left, r.bottom), (r.centerx, r.top), (r.right, r.bottom)]
        pg.draw.polygon(surface, color, pts)

    # Triángulos (abajo)
    for j, idx in enumerate(iter_points_bottom()):
        r = index_to_screen_pos(idx, False)
        color = TRI_LIGHT if j % 2 == 0 else TRI_DARK
        pts = [(r.left, r.top), (r.centerx, r.bottom), (r.right, r.top)]
        pg.draw.polygon(surface, color, pts)

    # Barra central
    cx1 = MARGIN + 6 * POINT_W
    bar = pg.Rect(cx1, MARGIN, MID_GAP, BOARD_H)
    pg.draw.rect(surface, (200, 170, 120), bar)
    pg.draw.line(surface, (120, 90, 60), (bar.left, MARGIN), (bar.left, H - MARGIN), 2)
    pg.draw.line(surface, (120, 90, 60), (bar.right, MARGIN), (bar.right, H - MARGIN), 2)

def draw_text(surface: pg.Surface, text: str, x: int, y: int, size=20, color=HUD_TEXT, center=False, bold=False):
    font = pg.font.SysFont(FONT_NAME, size, bold=bold)
    surf = font.render(text, True, color)
    rect = surf.get_rect()
    rect.center = (x, y) if center else (x, y)
    surface.blit(surf, rect)

def draw_checkers(surface: pg.Surface, game: BackgammonGame, show_counts: bool):
    points = game.get_points()
    max_visible = max(5, (POINT_H - 20) // (CHECKER_R + 4))

    for idx in range(24):
        is_top = point_is_top(idx)
        r = index_to_screen_pos(idx, is_top)
        val = points[idx]
        if val == 0:
            continue

        owner = 1 if val > 0 else -1
        color = BLUE if owner == 1 else RED
        count = abs(val)

        if is_top:
            for i in range(min(count, max_visible)):
                cx = r.centerx
                cy = r.top + 10 + i * (CHECKER_R + 4)
                pg.draw.circle(surface, color, (cx, cy), CHECKER_R)
                pg.draw.circle(surface, BLACK, (cx, cy), CHECKER_R, 2)
        else:
            for i in range(min(count, max_visible)):
                cx = r.centerx
                cy = r.bottom - 10 - i * (CHECKER_R + 4)
                pg.draw.circle(surface, color, (cx, cy), CHECKER_R)
                pg.draw.circle(surface, BLACK, (cx, cy), CHECKER_R, 2)

        if count > max_visible or show_counts:
            txt = f"{count}"
            draw_text(surface, txt, r.centerx - 8, r.centery - 10, size=18, color=WHITE, bold=True)

    # Barra
    bar = game.get_bar()
    j1_bar = bar.get(1, 0)
    j2_bar = bar.get(-1, 0)
    cx1 = MARGIN + 6 * POINT_W
    bar_rect = pg.Rect(cx1, MARGIN, MID_GAP, BOARD_H)

    for i in range(min(j1_bar, 7)):
        cx = bar_rect.centerx
        cy = bar_rect.bottom - 20 - i * (CHECKER_R + 6)
        pg.draw.circle(surface, BLUE, (cx, cy), CHECKER_R)
        pg.draw.circle(surface, BLACK, (cx, cy), CHECKER_R, 2)
    if j1_bar > 7:
        draw_text(surface, f"{j1_bar}", bar_rect.centerx - 8, bar_rect.bottom - 20 - 8 * (CHECKER_R + 6), color=WHITE, bold=True)

    for i in range(min(j2_bar, 7)):
        cx = bar_rect.centerx
        cy = bar_rect.top + 20 + i * (CHECKER_R + 6)
        pg.draw.circle(surface, RED, (cx, cy), CHECKER_R)
        pg.draw.circle(surface, BLACK, (cx, cy), CHECKER_R, 2)
    if j2_bar > 7:
        draw_text(surface, f"{j2_bar}", bar_rect.centerx - 8, bar_rect.top + 20 + 8 * (CHECKER_R + 6), color=WHITE, bold=True)

def draw_hud(surface: pg.Surface, game: BackgammonGame, msg: str = "", msg_color=HUD_TEXT):
    pg.draw.rect(surface, HUD, (0, 0, W, 40))
    pl = game.current_player()
    name = getattr(pl, "_name", getattr(pl, "name", "Jugador"))
    pid = getattr(pl, "_id", getattr(pl, "id", 1))
    moves = game.get_available_moves()
    font = pg.font.SysFont(FONT_NAME, 20)

    txt1 = font.render(f"Turno: {name} (id={pid})", True, HUD_TEXT)
    txt2 = font.render(f"Dados: {moves if moves else '—'}", True, HUD_TEXT)
    surface.blit(txt1, (12, 10))
    surface.blit(txt2, (280, 10))
    if msg:
        txt3 = font.render(msg, True, msg_color)
        surface.blit(txt3, (520, 10))

def screen_to_point(x: int, y: int) -> int | None:
    for idx in iter_points_top():
        if index_to_screen_pos(idx, True).collidepoint(x, y):
            return idx
    for idx in iter_points_bottom():
        if index_to_screen_pos(idx, False).collidepoint(x, y):
            return idx
    return None

# ========= Control principal =========
def run():
    pg.init()
    pg.display.set_caption("Backgammon - Pygame UI")
    screen = pg.display.set_mode((W, H))
    clock = pg.time.Clock()
    show_counts = False

    game = BackgammonGame()
    status_msg = ""
    status_color = HUD_TEXT
    selected_from = None

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.KEYDOWN:
                if e.key in (pg.K_ESCAPE, pg.K_q):
                    running = False
                elif e.key == pg.K_r:
                    try:
                        game.roll_dice()
                        status_msg = "Dados lanzados."
                        status_color = OK
                    except Exception as ex:
                        status_msg = f"Error: {ex}"
                        status_color = ERR
                elif e.key == pg.K_v:
                    show_counts = not show_counts
                elif e.key == pg.K_n:
                    game.change_turn()
                    status_msg = "Turno cambiado."
                    status_color = OK

            elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = e.pos
                pt = screen_to_point(mx, my)
                # <<< FIX: obtener owner sin tocar atributos privados >>>
                pl = game.current_player()
                owner = getattr(pl, "_id", getattr(pl, "id", 1))
                has_bar = game.get_bar().get(owner, 0) > 0

                if has_bar:
                    if pt is not None:
                        try:
                            game.reenter(pt)
                            status_msg = f"Reingreso en {pt}."
                            status_color = OK
                        except Exception as ex:
                            status_msg = f"Error: {ex}"
                            status_color = ERR
                else:
                    if pt is not None:
                        if selected_from is None:
                            selected_from = pt
                            status_msg = f"Origen: {pt}. Elegí destino…"
                            status_color = HUD_TEXT
                        else:
                            to_pt = pt
                            try:
                                game.move(selected_from, to_pt)
                                status_msg = f"Movido {selected_from} → {to_pt}."
                                status_color = OK
                            except Exception as ex:
                                status_msg = f"Error: {ex}"
                                status_color = ERR
                            selected_from = None

        # Dibujo
        draw_board(screen)
        draw_checkers(screen, game, show_counts)
        draw_hud(screen, game, status_msg, status_color)

        # Selección (origen)
        if selected_from is not None:
            r = index_to_screen_pos(selected_from, point_is_top(selected_from))
            pg.draw.rect(screen, (255, 255, 0), r, 3)

        pg.display.flip()
        clock.tick(60)

    pg.quit()
    sys.exit(0)

if __name__ == "__main__":
    run()
