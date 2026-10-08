from juego import Game

size = {"3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}


def mostrar_tablero(juego):
    tablero = juego.get_board()

    print("\nTablero:")
    for fila in tablero:
        print(" ".join("●" if valor == 1 else "○" for valor in fila))
    print()


def main():
    juego = Game()

    print("=== LIGHTS OUT ===")
    print("Cómo se juega -> 0")

    for (key, value) in size.items():
        print(f"{key}x{key} -> {value}")

    while True:
        opcion = input("Elige el tamaño del tablero: ")

        if opcion == "0":
            print("\n=== ¿CÓMO SE JUEGA? ===")
            print("El objetivo es apagar todas las luces del tablero.")
            print("Para hacerlo, elige una fila y una columna.")
            print("Al presionar una posición:")
            print("- La luz seleccionada cambia de estado.")
            print("- La luz de arriba cambia de estado.")
            print("- La luz de abajo cambia de estado.")
            print("- La luz de la izquierda cambia de estado.")
            print("- La luz de la derecha cambia de estado.")
            print("Las posiciones que están fuera del tablero simplemente no existen.")
            print("\n● = luz encendida")
            print("○ = luz apagada")
            print("\nSe gana cuando todas las luces estén apagadas.\n")
            continue

        if opcion in size:
            break

        print("Tamaño inválido.")

    juego.SelectSizeGame(size[opcion])

    while juego.CheckWin() == 0:

        mostrar_tablero(juego)

        try:
            x = int(input(f"Elige la fila (1-{juego.size}): ")) - 1
            y = int(input(f"Elige la columna (1-{juego.size}): ")) - 1

            juego.set_ady(x, y)

        except ValueError as e:
            print(f"Error: {e}")

    mostrar_tablero(juego)
    print("Ganaste! Todas las luces están apagadas.")


if __name__ == "__main__":
    main() 