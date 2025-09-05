from core.game import BackgammonGame

def main():
    juego = BackgammonGame()

    print("=== Bienvenido a Backgammon ===")
    while True:
        jugador = juego.current_player()
        print(f"\nTurno de: {jugador}")
        input("Presiona Enter para tirar los dados...")
        dados = juego.roll_dice()
        print("Dados:", dados)
        juego.show_board()
        juego.change_turn()

if __name__ == "__main__":
    main()
