"""def main():
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
    print(life)


def life_crear(mapa):
    #mapa = "\n".join(list(mapa))                              me parece q no va
    # estado = "\n".split(list(mapa))
    for char in mapa:
        if char == ".":
            mapa.replace(".", "False")

        else:
            mapa.replace("#", "True")


    print(mapa)


life_crear(
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
)"""

mapa1 = [
    "..........",
    "..........",
    "..........",
    ".....#....",
    "......#...",
    "....###...",
    "..........",
    "..........",
]


"""def a(mapa):
    estado = []
    for i in range(0, len(mapa)):
        estado.append(list(mapa[i]))
    return estado


a(mapa1)


def recorre_fil_col(lista):
    coord = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            coord.append(f"{i},{j}")
    return coord


print(recorre_fil_col(a(mapa1)))"""


def life_crear(mapa):
    mapa = list(mapa)
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

    estado = []
    for i in range(0, len(mapa)):
        estado.append(list(mapa[i]))
    for j in range(len(estado)):
        for k in range(len(estado[j])):
            if estado[j][k] == "#":
                estado[j][k] = True
            else:
                estado[j][k] = False

    return estado


life_crear(mapa1)


def life_mostrar(life):
    estado = life_crear(life)
    tablero = []
    for i in range(len(estado)):
        for j in range(len(estado[i])):
            if not estado[i][j] == True:
                estado[i][j] = "."
            else:
                estado[i][j] = "#"
        tablero.append("".join(estado[i]))

    return tablero


print(life_mostrar(mapa1))
life_mostrar(mapa1)


def cant_adyacentes(life, f, c):
    # Crea el tablero a partir de 'life'
    listas_life = life_crear(life)
    print(listas_life)

    # Variable para contar los adyacentes
    """adyacentes = 0

    # Posibles desplazamientos en las 8 direcciones
    desplazamiento = [
        (-1, -1),  # Noroeste
        (1, -1),  # Sureste
        (0, -1),  # Norte
        (-1, 0),  # Oeste
        (1, 0),  # Este
        (1, 1),  # Suroeste
        (0, 1),  # Sur
        (-1, 1),  # Noreste
    ]

    # Mostrar el tablero para ver cómo se representa
    print("Tablero:")
    for fila in listas_life:
        print(fila)

    # Verificar las celdas adyacentes
    for df, dc in desplazamiento:
        nueva_c_fil = f + df
        nueva_c_col = c + dc

        # Verifica que la celda esté dentro de los límites del tablero 8x8
        if 0 <= nueva_c_fil < len(listas_life) and 0 <= nueva_c_col < len(
            listas_life[0]
        ):
            print(f"Verificando celda ({nueva_c_fil}, {nueva_c_col})")
            # Verifica si la celda está activa
            if listas_life[nueva_c_fil][nueva_c_col]:
                print(f"Celda activa en ({nueva_c_fil}, {nueva_c_col})")
                adyacentes += 1
            else:
                print(f"Celda no activa en ({nueva_c_fil}, {nueva_c_col})")

    print(f"Total de adyacentes para ({f}, {c}): {adyacentes}")"""
    # return adyacentes


"""def cant_adyacentes(life, f, c):
    listas_life = life_crear(life)
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
        nueva_c_fil = f + df
        nueva_c_col = c + dc

        if 0 <= nueva_c_fil < len(listas_life) and 0 <= nueva_c_col < len(
            listas_life[0]
        ):
            if listas_life[nueva_c_fil][nueva_c_col]:
                adyacentes += 1

    return adyacentes"""


cant_adyacentes(mapa1, 4, 4)


"""
    Calcula la cantidad de células adyacentes a la celda en la fila `f` y la
    columna `c`.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
# return "???"


def celda_siguiente(life, f, c):
    """
    Calcula el estado siguiente de la celda ubicada en la fila `f` y la
    columna `c`.

    Devuelve True si en la celda (f, c) habrá una célula en la siguiente
    iteración, o False si la celda quedará vacía.
    """

    celda = life[f][c]
    n = cant_adyacentes(life, f, c)
    if celda == ".":
        if n == 3:
            celda = True
        else:
            celda = False
    elif celda == "#":
        if (n > 3) or (n == 1 or n == 0):
            celda = False
        elif (n == 2) or (n == 3):
            celda = True
    # print(f"Celda ({f},{c}) estado: {life[f][c]}, Vecinos: {n}")

    return celda


"""assert (celda_siguiente(mapa1, 4, 4)) == True
assert (celda_siguiente(mapa1, 0, 0)) == False
assert (celda_siguiente(mapa1, 1, 1)) == False
assert (celda_siguiente(mapa1, 3, 2)) == False
assert (celda_siguiente(mapa1, 4, 5)) == False"""


def life_siguiente(life):
    estado_actual = life_crear(life)
    print(estado_actual)
    estado_nuevo = []
    for f in range(len(estado_actual)):
        estado_nuevo.append([])
        for c in range(len(estado_actual[f])):
            estado_nuevo[f].append(celda_siguiente(estado_actual, f, c))
            # print(
            # f"Celda original: {estado_actual[f][c]} - Nuevo valor: {celda_siguiente(estado_actual, f, c)}"
            # )
            print()

    return estado_nuevo


life_siguiente(mapa1)

"""
    Calcula el siguiente estado del juego.

    Recibe el estado actual del juego (lista de listas de False/True) y
    devuelve un _nuevo_ estado que representa la siguiente iteración según las
    reglas del juego.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
# return "???"
