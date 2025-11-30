NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"
ELIMINAR = "Ingrese el tweet a eliminar:"
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."


def mostrar_inicio():
    ingreso = input("1. Crear Tweet\n2. Buscar Tweet\n3. Eliminar Tweet\n4. Salir\n")
    return ingreso


def main():
    tweets_existentes = {}
    id = 0
    while True:
        print()
        ingreso = mostrar_inicio()
        if ingreso == "1":
            tweets_existentes, id = crear_tweet(tweets_existentes, id)
        elif ingreso == "2":
            buscar_tweet(tweets_existentes)
        elif ingreso == "3":
            eliminar_tweet(tweets_existentes)
        elif ingreso == "4":
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


# todo pasado a diccionarios
def crear_tweet(tweets_existentes, id):
    ingreso = input("Agrega un tweet: ")
    if ingreso == ATRAS:
        return ingreso
    elif ingreso == "" or not ingreso.isalnum():
        print(INPUT_INVALIDO)
        return tweets_existentes, id

    tokenizacion_pal, tokenizacion_seg = tokenizacion_completa(ingreso)
    tweet = {
        "original": ingreso,
        "tokenizacion_pal": tokenizacion_pal,
        "tokenizacion_seg": tokenizacion_seg,
    }
    tweets_existentes[id] = tweet
    print(f"Ok {id}")
    id += 1
    return tweets_existentes, id


def buscar_tweet(diccionario):
    resultado = {}
    palabras_clave = input("Ingrese la/s palabra/s clave a buscar:\n")
    if palabras_clave == ATRAS:
        return diccionario
    tokenizar_pal, tokenizar_seg = tokenizacion_completa(palabras_clave)
    for clave in diccionario:
        for segmento in tokenizar_seg:
            if any(
                segmento in tokenizar_seg
                for segmento in diccionario[clave]["tokenizacion_seg"]
            ):
                resultado[clave] = diccionario[clave]["original"]
        for palabra in tokenizar_pal:
            if any(
                palabra in tokenizar_pal
                for palabra in diccionario[clave]["tokenizacion_pal"]
            ):
                resultado[clave] = diccionario[clave]["original"]
    if not resultado == {}:
        print(RESULTADOS_BUSQUEDA)
        for id, tweet in resultado.items():
            print(id, tweet)
    else:
        print(NO_ENCONTRADOS)
    return resultado


def eliminar_tweet(diccionario):
    a_eliminar = {}
    indice_a_borrar = []
    resultado = buscar_tweet(diccionario)
    if resultado == {}:
        return diccionario
    eliminar = input("Ingrese el numero de tweet que quiere eliminar:\n")
    if eliminar == ATRAS:
        return diccionario
    para_eliminar = eliminar.split(",")
    for elemento in para_eliminar:
        elemento = elemento.strip()
        if "-" in elemento:
            rango = elemento.split("-")
            desde, hasta = map(int, rango)

            for indice in range(desde, hasta + 1):
                if indice in resultado:
                    a_eliminar[indice] = resultado[indice]
                    indice_a_borrar.append(indice)

        elif elemento.isdigit():
            indice = int(elemento)
            if indice in resultado:
                a_eliminar[indice] = resultado[indice]
                indice_a_borrar.append(indice)
            else:
                print(NUMERO_INVALIDO)

    if not indice_a_borrar == []:
        print(TWEETS_ELIMINADOS)
        for indice in indice_a_borrar:
            print(f"{indice}.", diccionario[indice]["original"])
    for indice in sorted(indice_a_borrar, reverse=True):
        diccionario.pop(indice)
    return a_eliminar, diccionario


def tokenizacion_por_segmento(texto):
    texto = str(texto).lower()
    for char in texto:
        if char.isalnum() == False:
            texto = texto.replace(char, "")
    tokenizacion = []
    for i in range(len(texto) - 2):
        tokenizacion.append(texto[i : i + 3])
    return tokenizacion


def tokenizacion_simple(texto):
    simple = {}
    texto = str(texto).lower()
    for letra in texto:
        if letra.isalnum() == False:
            texto = texto.replace(letra, "")
    tokenizacion = texto.split()

    return tokenizacion


def tokenizacion_completa(texto):
    palabra = tokenizacion_simple(texto)
    segmento = tokenizacion_por_segmento(texto)
    return palabra, segmento


def validar_entrada(texto):
    if texto == ATRAS:
        return texto
    elif texto == "" or not texto.isalnum():
        print(INPUT_INVALIDO)


main()
