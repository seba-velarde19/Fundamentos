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


def life_mostrar(life):
    # ya recibe true y false
    tablero = []
    for i in range(len(life)):
        for j in range(len(life[i])):
            if not life[i][j] == True:
                life[i][j] = "."
            else:
                life[i][j] = "#"
        tablero.append("".join(life[i]))

    return tablero


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


def cant_adyacentes(life, f, c):
    # ya recibe lista true y false
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


def celda_siguiente(life, f, c):
    """
    Calcula el estado siguiente de la celda ubicada en la fila `f` y la
    columna `c`.

    Devuelve True si en la celda (f, c) habrá una célula en la siguiente
    iteración, o False si la celda quedará vacía.
    """

    celda = life[f][c]
    n = cant_adyacentes(life, f, c)
    if celda == False:
        if n == 3:
            celda = True
        else:
            celda = False
    elif celda == True:
        if (n > 3) or (n == 1 or n == 0):
            celda = False
        elif (n == 2) or (n == 3):
            celda = True

    return celda


def life_siguiente(life):
    # ya es un tablero true y false
    estado_nuevo = []
    for f in range(len(life)):
        estado_nuevo.append([])
        for c in range(len(life[f])):
            estado_nuevo[f].append(celda_siguiente(life, f, c))

    return estado_nuevo


print(life_siguiente(mapa1))
