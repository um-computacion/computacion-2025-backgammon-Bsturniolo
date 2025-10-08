from core.game import BackgammonGame

def main():
    juego = BackgammonGame()

    print("=== Bienvenido a Backgammon ===")
    
    while True:
        jugador = juego.current_player()
        print(f"\nTurno de: {jugador._name}")
        input("Presiona Enter para tirar los dados...")

        dados = juego.roll_dice()
        print("🎲 Dados:", dados)

        # Mostrar el tablero con más detalle
        puntos = juego.get_board().get_points()
        print("\n=== Tablero ===")
        for i, val in enumerate(puntos, start=1):
            ficha = ""
            if val > 0:
                ficha = "O" * val
            elif val < 0:
                ficha = "X" * abs(val)
            print(f"Punto {i:2}: {ficha}")
        print("================")

        juego.change_turn()

if __name__ == "__main__":
    main()
