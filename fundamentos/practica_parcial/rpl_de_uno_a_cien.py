import csv


def obtener_bigramas(texto):
    res = []
    lista_str = texto.split()
    if len(lista_str) < 2:
        print("no es un bigrama")
        return texto
    for i in range(len(lista_str) - 1):
        res.append((lista_str[i], lista_str[i + 1]))
    print(res)


obtener_bigramas("Uno se alegra de resultar útil")


def partir_tuplas(lista):
    res = []
    primera = []
    segunda = []
    for tupla in lista:
        primera.append(tupla[0])
        segunda.append(tupla[1])
    res.append(primera)
    res.append(segunda)
    print(tuple(res))


partir_tuplas([(1, 2), (1, 2), (1, 2), (8, 9)])


def separar_cadena():
    frecuencia = input("ingrese una frecuencia: ")
    texto = input("ingrese una frase: ")
    letras = ""
    res = []
    contador = 0
    for car in texto:
        letras += car
        contador += 1
        if contador == int(frecuencia):
            res.append(letras)
            letras = ""
            contador = 0
    if letras:  # Si quedaron letras sueltas al final
        res.append(letras)

    print("-".join(res))


def validar_ingreso(numero):
    if not numero.isdigit() or int(numero) < 0:
        return True
    return False


def a_multiplos_de_b():
    while True:
        in1 = input("n1: ")
        if validar_ingreso(in1):
            print("numero entero positivo")
            continue
        break

    while True:
        in2 = input("n2: ")
        if validar_ingreso(in2):
            print("numero entero positivo")
            continue
        break
    for i in range(1, int(in1) + 1):
        multiplos = int(in2) * i
        print(multiplos)


def invertir_palabras(cadena):
    res = []
    lista = cadena.split()
    for palabra in lista:
        res.append(palabra[::-1])
    print(" ".join(res))


invertir_palabras("Qué día tan bonito")

sett = {1, 2, 3, 4}
print(list(sett))


def ganadores(archivo, lista):
    res = {}
    with open(archivo, "r") as archivo:
        lector = csv.DictReader(
            archivo, fieldnames=["nombre", "apuesta"], delimiter=","
        )
        for linea in lector:
            apuesta = linea["apuesta"].split("-")
            nombre = linea["nombre"]
            for num in apuesta:
                if num in lista:
                    res[nombre] = res.get(nombre, 0) + 1

    with open("premios.csv", "w") as ganadores:
        escritor = csv.DictWriter(
            ganadores, fieldnames=["nombre", "cantidad"], delimiter=","
        )
        escritor.writeheader()
        for nombre, cantidad in res.items():
            escritor.writerow({"nombre": nombre, "cantidad": cantidad})
