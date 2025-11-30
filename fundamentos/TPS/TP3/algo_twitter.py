import os
import sys

NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."

ELIMINAR = "Ingrese el tweet a eliminar:\n>>> "
BUSCAR = "Ingrese la/s palabra/s clave a buscar:\n>>> "
OPCION_CREAR_TWEET = "1"
OPCION_BUSCAR_TWEET = "2"
OPCION_ELIMINAR_TWEET = "3"
OPCION_IMPORTAR_TWEET = "4"
OPCION_EXPORTAR_TWEET = "5"
OPCION_SALIR = "6"

ELEGIR_OPCION = """1. Crear Tweet\n2. Buscar Tweet
3. Eliminar Tweet\n4. Importar tweets
5. Exportar tweets\n6. Salir\n>>> """

INDICE_A_ELIMINAR = "Ingrese el numero de tweet que quiere eliminar:\n>>> "
SELECCION = "\nSeleccione una de las opciones:\n\n"
INGRESO_CREACION = "Ingrese un tweet a almacenar:\n>>> "


ERROR_IMPORTACION = "El/los archivos a importar deben existir y ser .txt válidos"
DIRECCION_ERRONEA = "No se pudo exportar a esa dirección."
TOKENIZACION_INVALIDA = "El argumento de cantidad de tokens es inválido."
DB_INVALIDA = "Error al intentar abrir el programa."


ARCHIVO_A_CARGAR = "Ingrese la ruta del archivo a cargar:\n>>> "
ARCHIVO_A_GUARDAR = "Ingrese la ruta del archivo a guardar:\n>>> "
DB_PATH = "db"


def analizar_argumentos(args):
    """verifica que el argumento para la parametrizacion sea
    valido, sino setea por defecto el numero 3"""

    parametro_tokenizacion = 3
    if len(args) > 1:
        if not args[1].isdigit():
            print(TOKENIZACION_INVALIDA)
            sys.exit()
        try:
            argumento = int(args[1])
        except ValueError:
            print(TOKENIZACION_INVALIDA)
            sys.exit()
        if argumento > 0:
            parametro_tokenizacion = argumento
        else:
            print(TOKENIZACION_INVALIDA)
            sys.exit()
    return parametro_tokenizacion


def main(arg=[]):
    """ejecuta el programa principal, entrando a cada funcion dependiendo de
    la eleccion del usuario"""
    arg_tokenizacion = analizar_argumentos(arg)
    tweets_existentes = {}
    tokenizados_existentes = {}
    inverso_tokenizados = {}
    cargar_db(
        tweets_existentes, tokenizados_existentes, inverso_tokenizados, arg_tokenizacion
    )
    cargar_opciones(
        arg_tokenizacion, tweets_existentes, tokenizados_existentes, inverso_tokenizados
    )


def cargar_opciones(
    arg_tokenizacion, tweets_existentes, tokenizados_existentes, inverso_tokenizados
):
    """carga todas las opciones del programa cargandob el ingreso a cada funcion
    segun la entrada del usuario"""

    while True:
        ingreso = mostrar_inicio()
        if ingreso == OPCION_CREAR_TWEET:
            crear_tweet(
                tweets_existentes,
                tokenizados_existentes,
                inverso_tokenizados,
                arg_tokenizacion,
            )
        elif ingreso == OPCION_BUSCAR_TWEET:
            buscar_tweet(tweets_existentes, tokenizados_existentes, BUSCAR)
        elif ingreso == OPCION_ELIMINAR_TWEET:
            eliminar_tweet(
                tweets_existentes, tokenizados_existentes, inverso_tokenizados, ELIMINAR
            )
        elif ingreso == OPCION_IMPORTAR_TWEET:
            importar_tweets(
                tweets_existentes,
                tokenizados_existentes,
                inverso_tokenizados,
                arg_tokenizacion,
            )
        elif ingreso == OPCION_EXPORTAR_TWEET:
            exportar_tweet(tweets_existentes)
        elif ingreso == OPCION_SALIR:
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


def mostrar_inicio():
    """muestra al usuario las opciones del programa y guarda el
    valor ingresado"""

    ingreso = input(f"{SELECCION}{ELEGIR_OPCION}")
    return ingreso


def obtener_id_maximo():
    """analiza el maximo valor entre los ids existentes desde
    la db y devulve el siguiente id para el siguiente tweet"""
    ids = []
    if os.path.exists(DB_PATH):
        for archivo in os.listdir(DB_PATH):
            if archivo.lower().endswith(".txt"):
                id_archivo = obtener_id_desde_nombre(archivo)
                if id_archivo is not None:
                    ids.append(id_archivo)
    if ids:
        return max(ids) + 1
    return 0


def obtener_id_desde_nombre(nombre_archivo):
    """Extrae el ID numérico de un archivo con nombre de
    la forma '123.txt'."""
    if not nombre_archivo.lower().endswith(".txt"):
        return None
    numero_id = nombre_archivo.split(".")[0]
    if numero_id.isdigit():
        return int(numero_id)
    return None


def validar_existencia_db():
    """verifica la existencia de ld db en el directorio
    donde esta el ejecutable"""
    if not os.path.isdir(DB_PATH):
        print(DB_INVALIDA)
        sys.exit()


def validar_corrupcion_db(archivo_tweet):
    """si el archivo no termina con .txt entonces tira error y
    cierra el programa"""
    if not archivo_tweet.lower().endswith(".txt"):
        print(DB_INVALIDA)
        sys.exit()


def cargar_db(tweets_existentes, tokenizados_existentes, inverso_tokenizados, arg):
    """se encarga de cargar los tweets existentes en la db, cada
    uno con su id correspondiente"""
    validar_existencia_db()
    tweets = os.listdir(DB_PATH)
    for tweet in tweets:
        validar_corrupcion_db(tweet)
        id = obtener_id_desde_nombre(tweet)
        if id is None:
            continue
        tweet = os.path.join(DB_PATH, tweet)
        with open(tweet, "r") as archivo:
            for linea in archivo:
                if not linea:
                    continue
                linea = linea.strip("\n")
                tweets_existentes[id] = linea
                agregar_tokenizacion(
                    tokenizados_existentes, inverso_tokenizados, id, linea, arg
                )


def guardar_en_db(id, ingreso):
    """guarda el contenido de un tweet en un archivo nombrandolo con
    el numero de id del tweet"""
    with open(f"db/{id}.txt", "w") as archivo:
        archivo.write(f"{ingreso}\n")


def eliminar_de_db(eliminados):
    """recibe el set que contiene los ids eliminados y los
    'elimina' de la db, borrando el contenido del archivo
    correspondiente al id"""
    for id in eliminados:
        with open(f"db/{id}.txt", "w") as archivo:
            archivo.write("")


def crear_tweet(
    tweets_existentes,
    tokenizados_existentes,
    inverso_tokenizados,
    arg,
    ingreso=None,
):
    """recibe diccionario con los tweets ya creados
    y el diccionario con los tweets tokenizados.

    tokeniza el ingreso y lo guarda
    en diccionarios distintos, uno para los tweets y otros dos
    para las tokenizaciones despues imprime por pantalla
    el numero de tweet guardado"""

    id = obtener_id_maximo()

    if ingreso is None:
        validacion, ingreso = verificar_ingreso(INGRESO_CREACION)
        if validacion:
            agregar_tokenizacion(
                tokenizados_existentes, inverso_tokenizados, id, ingreso, arg
            )
            tweets_existentes[id] = ingreso
            guardar_en_db(id, ingreso)
            print(f"OK {id}")

    else:
        agregar_tokenizacion(
            tokenizados_existentes, inverso_tokenizados, id, ingreso, arg
        )
        tweets_existentes[id] = ingreso
        guardar_en_db(id, ingreso)


def buscar_tweet(tweets_existentes, tokenizados_existentes, mensaje):
    """recibe el diccionario de tweets existentes y el diccionario de
    las tokenizaciones.

    si el ingreso del usuario es valido, tokeniza el ingreso y
    busca coincidencias entre tokens ingresados con los existentes
    (mediante funciones auxiliares), despues imprime coincidencias."""

    validacion, ingreso = verificar_ingreso(mensaje)
    if not validacion:
        return None, "**"

    if validacion:
        tokens_input = tokenizar_simple(ingreso)
        resultado = obtener_ids_coincidentes(tokens_input, tokenizados_existentes)
        imprimir_resultados(resultado, tweets_existentes)
    return resultado, ingreso


def eliminar_tweet(
    tweets_existentes, tokenizados_existentes, inverso_tokenizados, mensaje
):
    """recibe todos los diccionarios.

    llama a la funcion buscar_tweets, valida que haya un resultado,
    se valida la entrada del usuario y en caso de ser correcta
    elimina las claves de todos los diccionarios."""

    ids_a_eliminar = set()
    busqueda, palabras_clave = buscar_tweet(
        tweets_existentes, tokenizados_existentes, BUSCAR
    )
    if not busqueda or palabras_clave == ATRAS:
        return
    validacion = validar_ingreso_eliminacion(ids_a_eliminar, busqueda, mensaje)
    if validacion:
        eliminar_claves(
            tweets_existentes,
            busqueda,
            ids_a_eliminar,
            tokenizados_existentes,
            inverso_tokenizados,
        )
    return


def importar_tweets(tweets_existentes, tokenizados_existentes, inverso_tokens, arg):
    """recibe una entrada que debe ser obligatoriamente un directorio o un archivo
    separa archivos de directorios, recorre recursivamente estos ultimos
    en busca de archivos y agrega el contenido de los archivos.txt al programa"""

    while True:
        contador_total = 0
        validacion, directorios, archivos = validar_entrada_importacion()
        if validacion is None:
            break
        if not validacion:
            continue
        if validacion:
            for ruta_archivo in archivos:
                contador = agregar_tweets(
                    ruta_archivo,
                    tweets_existentes,
                    tokenizados_existentes,
                    inverso_tokens,
                    arg,
                )
                contador_total += contador
            for ruta in directorios:
                contador = recorrer_diccionarios(
                    ruta, tweets_existentes, tokenizados_existentes, inverso_tokens, arg
                )
                contador_total += contador

            print(f"OK {contador_total}")
            break


def exportar_tweet(tweets_existentes):
    """recibe la ruta a un archivo.txt y escribe linea por
    linea los tweets existentes en el programa, no tiene en cuenta ids
    si el archivo no existe se crea."""
    while True:

        try:
            validacion, archivo = validar_ingreso_exportacion()
        except FileNotFoundError:
            print(DIRECCION_ERRONEA)
            continue

        if not validacion:
            break
        if validacion:
            validar_escritura, contador = escribir_archivo_a_guardar(
                archivo, tweets_existentes
            )
            if validar_escritura:
                print(f"OK {contador}")
                break
            continue


def dividir_entrada_importacion(directorios, archivos, ruta_invalida, ingreso):
    """separa la entrada del usuario en casos que haya mas de una ruta
    y categoriza segun si es archivo o directorio"""
    ingreso = ingreso.split(" ")
    for ruta in ingreso:
        if os.path.isdir(ruta):
            directorios.append(ruta)
        elif os.path.isfile(ruta) and ruta.lower().endswith(".txt"):
            archivos.append(ruta)
        else:
            ruta_invalida.append(ruta)


def validar_entrada_importacion():
    """comprueba que la entrada del usuario sea valida mostrando
    el error en el caso invalido, en caso de ser valida, categoriza
    la entrada y devuelve la lista de directorios y la de archivos"""
    directorios = []
    archivos = []
    ruta_invalida = []

    ingreso = input(ARCHIVO_A_CARGAR)
    if ingreso == ATRAS:
        return None, directorios, archivos

    dividir_entrada_importacion(directorios, archivos, ruta_invalida, ingreso)

    if ruta_invalida:
        print(ERROR_IMPORTACION)
        return False, directorios, archivos

    return True, directorios, archivos


def recorrer_diccionarios(
    ruta, tweets_existentes, tokenizados_existentes, inverso_tokens, arg
):
    """separa todo el contenido del directorio de una lista en busca
    de archivos.txt para cargar en el programa, en caso de que haya
    otro directorio, actua de manera recursiva"""

    contador_total = 0
    for nombre in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre)
        if os.path.isdir(ruta_completa):
            contador = recorrer_diccionarios(
                ruta_completa,
                tweets_existentes,
                tokenizados_existentes,
                inverso_tokens,
                arg,
            )
            contador_total += contador
        elif os.path.isfile(ruta_completa) and ruta_completa.lower().endswith(".txt"):
            contador = agregar_tweets(
                ruta_completa,
                tweets_existentes,
                tokenizados_existentes,
                inverso_tokens,
                arg,
            )
            contador_total += contador
    return contador_total


def agregar_tweets(
    ruta, tweets_existentes, tokenizados_existentes, inverso_tokens, arg
):
    """abre el archivo pasado por parametro, lo lee linea por linea
    mientras va creando cada tweet individualmente, finalmente devuelve
    un contador que trae la cuenta de los tweets importados"""
    contador = 0
    with open(ruta, "r") as archivo:
        for linea in archivo:
            tweet = linea.strip("\n")
            if not tokenizar_simple(tweet):
                continue
            if tweet:
                crear_tweet(
                    tweets_existentes,
                    tokenizados_existentes,
                    inverso_tokens,
                    arg,
                    tweet,
                )
                contador += 1
    return contador


def validar_ingreso_exportacion():
    """verifica que el ingreso de exportacion sea un aechivo
    ademas comprueba que el ingreso sea un unico archivo"""
    while True:
        archivo = input(ARCHIVO_A_GUARDAR)
        if archivo == ATRAS:
            return False, archivo
        if len(archivo.split(" ")) > 1:
            print(DIRECCION_ERRONEA)
            continue
        if os.path.isdir(archivo) or not archivo.lower().endswith(".txt"):
            print(DIRECCION_ERRONEA)
            continue
        if not os.path.isfile(archivo) and archivo.lower().endswith(".txt"):
            with open(archivo, "w") as archivo_nuevo:
                archivo_nuevo.write("")
        return True, archivo


def escribir_archivo_a_guardar(archivo, tweets_existentes):
    """se encarga de escribir todos los tweets en el archivo
    ingresado, en caso de no existir genera el archivo."""
    contador = 0

    with open(archivo, "w") as archivo_a_escrbir:
        for tweet in tweets_existentes.values():
            archivo_a_escrbir.write(tweet + "\n")
            contador += 1
    return True, contador


def verificar_ingreso(mensaje):
    """valida el ingreso del usuario hasta que sea correcto,
    indicando que hubo un error en el respectivo caso."""

    while True:
        ingreso = input(mensaje)
        if ingreso == ATRAS:
            return False, ingreso
        if ingreso == "" or tokenizar_simple(ingreso) == []:
            print(INPUT_INVALIDO)
            continue
        return True, ingreso


def tokenizar_por_segmento(texto, arg):
    """recibe una string y tokeniza por segmentos de n>=3, eliminando
    caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    texto = normalizar(str(texto).lower())
    texto_nuevo = ""
    for char in texto:
        if not char.isalnum():
            texto_nuevo += " "
        else:
            texto_nuevo += char
    texto = " ".join(texto_nuevo.split())
    palabras = texto.split(" ")
    tokenizacion = []
    for palabra in palabras:
        for i in range(len(palabra)):
            for j in range(i + arg - 1, len(palabra)):
                token = palabra[i : j + 1]
                tokenizacion.append(token)
    return tokenizacion


def tokenizar_simple(texto):
    """recibe una string y la tokeniza por palabras, separadas por
    espacios, elimina caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    texto = normalizar(str(texto).lower())
    texto_nuevo = ""
    for letra in texto:
        if not letra.isalnum():
            texto_nuevo += " "
        else:
            texto_nuevo += letra
    texto = " ".join(texto_nuevo.split())
    palabras = texto.split()
    return palabras


def tokenizar_completo(texto, arg):
    """recibe una string y realiza los dos tipos de tokenizaciones
    de la misma.

    devuelve dos listas con las tokenizaciones respectivas."""
    palabra = tokenizar_simple(texto)
    segmento = tokenizar_por_segmento(texto, arg)
    return palabra, segmento


def normalizar(texto):
    """Reemplaza letras con tilde y dieresis por su equivalente sin tilde,
    usando .get()."""
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "Á": "a",
        "É": "e",
        "Í": "i",
        "Ó": "o",
        "Ú": "u",
        "ü": "u",
        "Ü": "u",
    }
    nuevo_texto = ""
    for c in texto:
        nuevo_texto += reemplazos.get(c, c)
    return nuevo_texto


def agregar_tokenizacion(tokenizados_existentes, inverso_tokens, id, ingreso, arg):
    """agrega los dos tipos de tokenizaciones de un string a un mismo
    diccionario, guardando los ids en un mismo set por cada clave,
    teniendo en cuenta los casos en que la palabra tiene menos de
    tres caracteres, ademas guarda los mismo valores de forma
    inversa para utilizar de forma mas eficiente mas adelante."""

    tokenizacion_pal, tokenizacion_segmento = tokenizar_completo(ingreso, arg)
    tokens = tokenizacion_pal + tokenizacion_segmento
    for token in tokens:
        tokenizados_existentes[token] = tokenizados_existentes.get(token, set())
        tokenizados_existentes[token].add(id)

    inverso_tokens[id] = set(tokens)


def imprimir_resultados(resultado_coincidencias, tweets_existentes):
    """verifica que haya coincidencias y las imprime en pantalla."""
    if not resultado_coincidencias:
        print(NO_ENCONTRADOS)
        return False

    print(RESULTADOS_BUSQUEDA)
    for id in sorted(resultado_coincidencias):
        print(f"{id}. {tweets_existentes[id]}")
    return True


def validar_ingreso_eliminacion(ids_a_eliminar, busqueda, mensaje):
    """Pide ingreso al usuario para realizar la eliminacion
    validando de que este ingreso sea correcto.
    imprime diferentes cosas en pantalla dependiendo del error."""

    while True:
        validacion_entrada, ingreso = verificar_ingreso(mensaje)
        if not validacion_entrada:
            return False

        ids_a_eliminar.clear()
        if not agregar_ids_a_eliminar(ids_a_eliminar, ingreso):
            print(INPUT_INVALIDO)
            continue

        validacion_coincidiente, mensaje_error = validar_coincidencia(
            ids_a_eliminar, busqueda
        )

        if not validacion_coincidiente and mensaje_error == NO_ENCONTRADOS:
            print(mensaje_error)
            return False

        if not validacion_coincidiente:
            print(mensaje_error)
            continue

        return True


def obtener_ids_coincidentes(tokens_input, tokenizados_existentes):
    """se encarga de encontrar todos los tokens que coincidan con
    lo ingresado y eso lo guarda en un set para usar en la funcion
    principal"""

    resultado = set()
    ids = []
    for token in tokens_input:
        if token in tokenizados_existentes:
            ids_token = tokenizados_existentes[token]
        else:
            ids_token = set()
        ids.append(ids_token)
    resultado = set.intersection(*ids)
    return resultado


def validar_coincidencia(ids_a_eliminar, busqueda):
    """recibe un set con los ids a eliminar y los resultados de busqueda.

    verifica que el set no este vacio y que sus elementos pertenezcan
    a la busqueda."""
    no_encontrado = 0
    if not ids_a_eliminar:
        return False, INPUT_INVALIDO
    for id in ids_a_eliminar:
        if id not in busqueda:
            no_encontrado += 1
    if no_encontrado > 0 and len(ids_a_eliminar) > 1:
        return False, NUMERO_INVALIDO
    if no_encontrado > 0:
        return False, NO_ENCONTRADOS
    return True, ""


def agregar_ids_a_eliminar(ids_a_eliminar, ingreso):
    """recibe el input del usuario, separa dependiendo de que sea un
    rango o un numero solo y actualiza los valores de los indices en
    el set ya creado."""

    para_eliminar = ingreso.split(",")
    mensaje = ""

    if ingreso.strip() == "":
        return False

    for elemento in para_eliminar:
        elemento = elemento.strip()
        if "-" in elemento:
            mensaje = agregar_rango_a_eliminar(elemento, ids_a_eliminar)
            if mensaje != "":
                return False
        elif elemento.isdigit():
            agregar_digito_aislado(elemento, ids_a_eliminar)
        else:
            return False

    return True


def agregar_rango_a_eliminar(rango, ids_a_eliminar):
    """recibe strings y el set que contiene los indices a eliminar
    verifica que sean caracteres validos y añade dichos indices a eliminar,
    en caso contrario devuelve input invalido."""

    rango_dividido = rango.split("-")
    if not validar_rango_a_eliminar(rango):
        return INPUT_INVALIDO

    desde = int(rango_dividido[0].strip())
    hasta = int(rango_dividido[1].strip())

    for indice in range(desde, hasta + 1):
        ids_a_eliminar.add(indice)

    return ""


def validar_rango_a_eliminar(rango):
    """verifica que el rango ingresado sea valido."""
    rango_dividido = rango.split("-")
    if len(rango_dividido) != 2:
        return False

    desde, hasta = rango_dividido[0].strip(), rango_dividido[1].strip()
    if desde == "" or hasta == "":
        return False
    if not (desde.isdigit() and hasta.isdigit()):
        return False

    desde, hasta = int(desde), int(hasta)
    return desde <= hasta


def agregar_digito_aislado(digito, ids_a_eliminar):
    """recibe el digito ingresado y el set que contiene los indices
    a eliminar y añade el numero."""

    indice = int(digito)
    ids_a_eliminar.add(indice)


def imprimir_eliminaciones(eliminados, tweets_existentes):
    """imprime los ids junto con los tweets que se van a eliminar"""
    if not eliminados:
        print(NUMERO_INVALIDO)
        return

    print(TWEETS_ELIMINADOS)
    for id in eliminados:
        print(f"{id}. {tweets_existentes[id]}")
        tweets_existentes.pop(id)

    return


def eliminar_claves(
    tweets_existentes,
    busqueda,
    ids_a_eliminar,
    tokenizados_existentes,
    inverso_tokenizados,
):
    """recibe el diccionario con los tweets creados, los resultados
    de busqueda, el set que contiene los indices a eliminar y
    el diccionario con los tweets ya tokenizados.

    verifica que los elementos del set esten en la busqueda y en el diccionario
    y los agrega a otro set para posteriormente mostrar por pantalla
    los tweets eliminados y eliminar los mismos tanto del diccionario
    de tweets como sus tokenizaciones."""

    eliminados = set()
    for id in ids_a_eliminar:
        if id in busqueda and id in tweets_existentes:
            eliminados.add(id)
    imprimir_eliminaciones(eliminados, tweets_existentes)
    eliminar_tokenizaciones(eliminados, tokenizados_existentes, inverso_tokenizados)
    eliminar_de_db(eliminados)


def eliminar_tokenizaciones(
    ids_a_eliminar, tokenizados_existentes, inverso_tokenizados
):
    """Elimina las tokenizaciones asociadas a los IDs dados,
    actualizando ambos diccionarios: el original y el inverso."""

    for id in ids_a_eliminar:
        if id not in inverso_tokenizados:
            continue

        tokens = inverso_tokenizados[id]
        for token in tokens:
            if token in tokenizados_existentes:
                tokenizados_existentes[token].discard(id)
                if not tokenizados_existentes[token]:
                    del tokenizados_existentes[token]
        del inverso_tokenizados[id]


if __name__ == "__main__":
    args = sys.argv
    main(args)
