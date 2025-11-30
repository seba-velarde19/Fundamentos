NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
FIN = "Finalizando..."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"
BUSQUEDA = "Ingrese la/s palabra/s clave a buscar:"
ELIMINAR = "Ingrese el tweet a eliminar:"


# todo pasado a diccionarios
def crear_tweet(tweets_existentes, id):
    """recibe el input del usuario lo tokeniza
    y guarda en un diccionario el id, el ingreso
    y la tokenizacion

    agrega a la lista pasada por parametros, el diccionario con el tweet

    devuelve la lista de tweets y el proximo id"""

    ingreso = input("Agrega un tweet: ")
    if ingreso == ATRAS:
        return tweets_existentes, id
    normalizados = normalizar(ingreso)
    tweet = {"id": id, "original": ingreso, "normalizado": normalizados}
    tweets_existentes.append(tweet)
    print(f"Ok {id}")
    id += 1
    return tweets_existentes, id


def buscar_tweet(lista, mensaje):
    """recibe el ingreso de las palabras claves, las tokeniza y revisa
    si hay tokenizaciones que coincidan con las tokenizaciones de algun
    tweeten el caso de que coincidan, los agrega a resultado(diccionario)
    como indice:tweet

    imprime los tweets encontrados
    devuelve resultado"""

    resultado = {}
    print(mensaje)
    palabras_clave = input("")
    if palabras_clave == ATRAS:
        return lista, mensaje
    palabras_normalizadas = normalizar(palabras_clave)
    for i in range(len(lista)):  # 1 x tweet
        for normalizacion in palabras_normalizadas:
            if normalizacion in lista[i]["normalizado"]:
                resultado[i] = lista[i]["original"]
                break
    if not resultado == {}:
        print(RESULTADOS_BUSQUEDA)
        for id, tweet in resultado.items():
            print(id, tweet)
    else:
        print(NO_ENCONTRADOS)
    return resultado


def eliminar_tweet(lista):
    a_eliminar = {}
    indice_a_borrar = []
    resultado = buscar_tweet(lista, ELIMINAR)
    if resultado == {}:
        return lista
    print("Ingrese el numero de tweet que quiere eliminar")
    eliminar = input("")
    if eliminar == ATRAS:
        return lista
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

    for indice in sorted(indice_a_borrar, reverse=True):
        lista.pop(indice)
    if not indice_a_borrar == []:
        print(TWEETS_ELIMINADOS)
        for indice in indice_a_borrar:
            print(f"{lista[indice]["id"]}.", lista[indice]["original"])
    return a_eliminar, lista


def normalizar(texto):
    """recibe una cadena de texto y elimina caracteres especiales
    para posteriormente dividirla en listas de 3 caracteres dentro de
    otra lista

    devuelve la lista de listas(tokenizacion)"""

    texto = str(texto).lower()
    caracteres_no_importantes = ",.?/:'[]()!@#$`~&"
    for char in caracteres_no_importantes:
        texto = texto.replace(char, "")
    tokenizacion = []
    for i in range(len(texto) - 2):
        tokenizacion.append(texto[i : i + 3])
    return tokenizacion
