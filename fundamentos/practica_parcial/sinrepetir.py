def sin_repetir(cadena):
    lista = []
    for letra in cadena:
        if not letra in lista:
            lista.append(letra)
    return "".join(lista)


print(sin_repetir("hhhhooooollaaa"))
