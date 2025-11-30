import os

ERROR_IMPORTACION = "El/los archivos a importar deben existir y ser .txt válidos"
DIRECCION_ERRONEA = "No se pudo exportar a esa dirección."
TOKENIZACION_INVALIDA = "El argumento de cantidad de tokens es inválido."
DB_INVALIDA = "Error al intentar abrir el programa."


ARCHIVO_A_CARGAR = "Ingrese la ruta del archivo a cargar:\n>>> "
ARCHIVO_A_GUARDAR="Ingrese la ruta del archivo a guardar:\n>>> "


def importar_tweets(tweets_existentes, id, tokenizados_existentes, inverso_tokens):
    validacion, ingreso = validar_entrada_importacion(ERROR_IMPORTACION)
    if validacion:
        for ruta in ingreso:
            id_actual, contador_total = recorrer_diccionarios(
                ruta, tweets_existentes, id, tokenizados_existentes, inverso_tokens
            )
        print(f"OK {contador_total}")
    return id_actual


def crear_tweet(
    tweets_existentes, id, tokenizados_existentes, inverso_tokens, ingreso=None
):
    """recibe diccionario con los tweets ya creados, el numero
    de id que corresponde y el diccionario con los tweets tokenizados.

    tokeniza el ingreso y lo guarda
    en diccionarios distintos, uno para los tweets y otros dos
    para las tokenizaciones despues imprime por pantalla
    el numero de tweet guardado"""

    if ingreso is None:
        validacion, ingreso = verificar_ingreso(INGRESO_CREACION)
        if validacion:
            agregar_tokenizacion(tokenizados_existentes, inverso_tokens, id, ingreso)
            tweets_existentes[id] = ingreso
            print(f"OK {id}")

    else:
        agregar_tokenizacion(tokenizados_existentes, inverso_tokens, id, ingreso)
        tweets_existentes[id] = ingreso

    return id + 1


def validar_entrada_importacion(mensaje):
    while True:
        ingreso = input(mensaje)
        ingreso = ingreso.split(" ")
        for path in ingreso:
            if not os.path.isdir(ingreso) or not ingreso.endswith(".txt"):
                print(mensaje)
                continue
        return True, ingreso


def recorrer_diccionarios(
    ruta, tweets_existentes, id, tokenizados_existentes, inverso_tokens
):
    id_actual = id
    contador_total = 0
    for nombre in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre)
        if os.path.isdir(ruta_completa):
            id_actual = recorrer_diccionarios(
                ruta_completa,
                tweets_existentes,
                id,
                tokenizados_existentes,
                inverso_tokens,
            )
        elif nombre.endswith(".txt"):
            id_actual, contador = agregar_tweets(
                ruta,
                tweets_existentes,
                id_actual,
                tokenizados_existentes,
                inverso_tokens,
            )
            contador_total += contador
    return id_actual, contador_total


def agregar_tweets(
    path, tweets_existentes, id, tokenizados_existentes, inverso_tokens, linea
):
    contador = 0
    with open(path, "r") as archivo:
        for linea in archivo:
            tweet = linea.strip("\n")
            contador += 1
            if tweet:
                id_actual = crear_tweet(
                    tweets_existentes, id, tokenizados_existentes, inverso_tokens, tweet
                )
    return id_actual, contador


def exportar_tweet(tweets_existentes):
    while True:
        validacion,archivo=validar_ingreso_exportacion():
        if validacion:
            validar_escritura,contador=escribir_archivo_a_guardar(archivo,tweets_existentes)
            if validar_escritura:
                print(f"OK {contador}")
            else:
                continue



def validar_ingreso_exportacion():
    while True:
        archivo=input(ARCHIVO_A_GUARDAR)
        if archivo==ATRAS:
            return False,archivo
        if len(archivo.split(" "))>1:
            print(DIRECCION_ERRONEA)
            continue
        if not os.path.isfile(archivo):
            print(DIRECCION_ERRONEA)
            continue
        return True,archivo



def escribir_archivo_a_guardar(archivo,tweets_existentes):
    contador=0
    try:
        with open(archivo,"w") as archivo:
            for tweet in tweets_existentes.values():
                archivo.write(tweet+"\n")
                contador+=1
        return True,contador
    except FileNotFoundError:
        print(DIRECCION_ERRONEA)
        return False,contador