def maximos_columnas(matriz):
    if not matriz:
        return []

    num_columnas = len(matriz[0])
    maximos = []

    for col in range(num_columnas):
        max_col = matriz[0][col]
        for fila in matriz:
            if fila[col] > max_col:
                max_col = fila[col]
        maximos.append(max_col)

    print(maximos)


matriz = [[1, 2, 8, 4], [6, 7, 3, 3], [6, 5, 4, 9]]
maximos_columnas(matriz)
