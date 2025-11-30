from inicio2 import main

NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"


def crear_tweet(tweets_existentes, id, original):
    ingreso = input("Agrega un tweet: ")
    normalizados = normalizar(ingreso)
    original.append(ingreso)
    tweets_existentes.append(normalizados)
    print(f"Ok {id}")
    id += 1
    return tweets_existentes, id, original


def buscar_tweet(lista):
    resultado = {}
    print("Busca tu tweet")
    palabras_clave = input("")
    normalizado = normalizar(palabras_clave)
    for i in range(len(lista)):
        if any(token in lista[i] for token in normalizado):
            resultado[i] = lista[i]
    for id, tweet in resultado.items():
        print(id, tweet)
    return resultado


def eliminar_tweet(lista):
    a_eliminar = {}
    resultado = buscar_tweet(lista)
    print("Ingrese el numero de tweet que quiere eliminar")
    eliminar = input("")
    para_eliminar = eliminar.split(",")
    for elemento in para_eliminar:
        elemento.strip()
        if "-" in elemento:
            desde, hasta = list(map(int, elemento.strip("-")))
            for indice in range(desde, hasta + 1):
                if indice in resultado:
                    a_eliminar[indice] = elemento
                    resultado.pop(indice)
        else:
            a_eliminar[elemento] = elemento
            resultado.pop(elemento)
    return a_eliminar


def normalizar(texto):
    texto = str(texto).lower()
    caracteres_no_importantes = ",.?/:'[]()!@#$`~&"
    for char in caracteres_no_importantes:
        texto = texto.replace(char, "")
    cambiados = []
    for i in range(len(texto) - 2):
        cambiados.append(texto[i : i + 3])
    return cambiados
