def main():
    """
    Función principal del programa. Crea el estado inicial de Game of Life
    y muestra la simulación paso a paso mientras que el usuario presione
    Enter.
    """
    life = life_crear(
        [
            "..........",
            "..........",
            "..........",
            ".....#....",
            "......#...",
            "....###...",
            "..........",
            "..........",
        ]
    )
    while True:
        for linea in life_mostrar(life):
            print(linea)
        print()
        input("Presione Enter para continuar, CTRL+C para terminar")
        print()
        life = life_siguiente(life)


# -----------------------------------------------------------------------------


def life_crear(mapa):
    """
    Crea el estado inicial de Game of life a partir de una disposición
    representada con los caracteres '.' y '#'.

    `mapa` debe ser una lista de cadenas, donde cada cadena representa una
    fila del tablero, y cada caracter puede ser '.' (vacío) o '#' (célula).
    Todas las filas deben tener la misma cantidad de caracteres.

    Devuelve el estado del juego, que es una lista de listas donde cada
    sublista representa una fila, y cada elemento de la fila es False (vacío)
    o True (célula).
    """
    mapa = list(mapa)
    estado = []
    for i in range(0, len(mapa)):
        estado.append(list(mapa[i]))
    for j in range(len(estado)):
        for k in range(len(estado[j])):
            if not estado[j][k] == ".":
                estado[j][k] = True
            else:
                estado[j][k] = False

    return estado


# -----------------------------------------------------------------------------


def life_mostrar(life):
    """Crea una representación del estado del juego para mostrar en pantalla.

    Recibe el estado del juego (inicialmente creado con life_crear()) y
    devuelve una lista de cadenas con la representación del tablero para
    mostrar en la pantalla. Cada una de las cadenas representa una fila
    y cada caracter debe ser '.' (vacío) o '#' (célula)."""

    tablero = []
    life2 = []

    for linea in life:
        life2.append(linea[:])
    for i in range(len(life)):
        for j in range(len(life[i])):
            if not life[i][j]:
                life2[i][j] = "."
            else:
                life2[i][j] = "#"
        tablero.append("".join(life2[i]))

    return tablero


# -----------------------------------------------------------------------------


def cant_adyacentes(life, f, c):
    """
    Calcula la cantidad de células adyacentes a la celda en la fila `f` y la
    columna `c`.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
    filas = len(life)
    columnas = len(life[0])
    adyacentes = 0
    desplazamiento = [
        (-1, -1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
    ]
    for df, dc in desplazamiento:
        nueva_c_fil = (f + df) % filas
        nueva_c_col = (c + dc) % columnas

        if life[nueva_c_fil][nueva_c_col]:
            adyacentes += 1

    return adyacentes


# -----------------------------------------------------------------------------


def celda_siguiente(life, f, c):
    """
    Calcula el estado siguiente de la celda ubicada en la fila `f` y la
    columna `c`.

    Devuelve True si en la celda (f, c) habrá una célula en la siguiente
    iteración, o False si la celda quedará vacía.
    """

    celda = life[f][c]
    n = cant_adyacentes(life, f, c)
    if not celda:
        if n == 3:
            celda = True
    elif celda:
        if (n > 3) or n in (1, 0):
            celda = False

    return celda


# -----------------------------------------------------------------------------


def life_siguiente(life):
    """Calcula el siguiente estado del juego.

    Recibe el estado actual del juego (lista de listas de False/True) y
    devuelve un _nuevo_ estado que representa la siguiente iteración según las
    reglas del juego.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa."""

    estado_nuevo = []
    for f in range(len(life)):
        estado_nuevo.append([])
        for c in range(len(life[f])):
            estado_nuevo[f].append(celda_siguiente(life, f, c))

    return estado_nuevo


# -----------------------------------------------------------------------------

# Esta parte del código se ejecuta al final,
# #asegurando que se ejecute el programa
# mediante la terminal correctamente y permitiendo que se puedan realizar
# los tests de forma automática y aislada.
if __name__ == "__main__":
    main()
