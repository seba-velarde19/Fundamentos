NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"
ELIMINAR = "Ingrese el tweet a eliminar:"
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."
OPCION_CREAR_TWEET = "1"
OPCION_BUSCAR_TWEET = "2"
OPCION_ELIMINAR_TWEET = "3"
OPCION_SALIR = "4"
ELEGIR_OPCION = "1. Crear Tweet\n2. Buscar Tweet\n3. Eliminar Tweet\n4. Salir\n"
INDICE_A_ELIMINAR = "Ingrese el numero de tweet que quiere eliminar:\n"


def mostrar_inicio():
    """muestra al usuario las opciones del programa y guarda el
    valor ingresado"""

    ingreso = input(ELEGIR_OPCION)
    return ingreso


def crear_tweet(tweets_existentes, id, tokenizados_seg):
    """recibe diccionario con los tweets ya creados, el numero
    de id que corresponde y el diccionario con los tweets tokenizados.

    le pide al usuario el ingreso de un tweet, lo tokeniza y guarda
    en diccionarios distintos, uno para los tweets y
    otro para las tokenizaciones despues imprime por
    pantalla el numero de tweet guardado y devuelve los
    diccionarios actualizados."""

    ingreso = input("Agrega un tweet:\n")
    if ingreso == ATRAS:
        return tweets_existentes, id, tokenizados_seg
    if ingreso == "" or tokenizacion_simple(ingreso) == []:
        print(INPUT_INVALIDO)
        return tweets_existentes, id, tokenizados_seg

    tokenizados_seg = agregar_tokenizacion(tokenizados_seg, id, ingreso)
    tweet = ingreso
    tweets_existentes[id] = tweet
    print(f"Ok {id}")
    id += 1
    return tweets_existentes, id, tokenizados_seg


def buscar_tweet(diccionario, tokenizados_seg):
    """recibe el diccionario de tweets existentes y el diccionario de
    las tokenizaciones.

    le pide al usuario el ingreso de palabras a buscar y las tokeniza
    para despues recorrer estas tokenizaciones y analizar su existencia
    en el diccionario de los tweets tokenizados, en el caso de encontrarlos
    los agrega a resultado para posteriormente imprimir los tweets encontrados
    junto con sus ids correspondientes."""

    resultado = set()
    palabras_clave = input("Ingrese la/s palabra/s clave a buscar:\n")
    if palabras_clave == ATRAS:
        return diccionario

    tokens_pal, tokens_seg = tokenizacion_completa(palabras_clave)
    tokens_total = set(tokens_pal + tokens_seg)

    for token in tokens_total:
        if token in tokenizados_seg:
            resultado.update(tokenizados_seg[token])

    if not resultado:
        print(NO_ENCONTRADOS)
    else:
        print(RESULTADOS_BUSQUEDA)
        for id in resultado:
            print(f"{id}.", diccionario[id])
    return resultado


def eliminar_tweet(diccionario, tokenizados_seg):
    """recibe el diccionario de los tweets existentes y las tokenizaciones de
    los tweets.

    realiza una busqueda para saber que es lo que se busca eliminar,
    si la busqueda no es vacia muestra lo encontrado y le
    pide al usuario el ingreso del indice a eliminar,
    en el caso de que el indice exista se elimina el/los tweets
    y se muestran por pantalla, en el caso contrario
    se muestra un mensaje de numero invalido"""

    eliminar = set()
    busqueda = buscar_tweet(diccionario, tokenizados_seg)
    if not busqueda:
        return diccionario, tokenizados_seg

    while True:
        ingreso_a_eliminar = input(INDICE_A_ELIMINAR)
        if ingreso_a_eliminar == ATRAS:
            return diccionario
        eliminar = ids_a_eliminar(ingreso_a_eliminar)
        if validar_ids(eliminar, busqueda):
            eliminar_claves(diccionario, busqueda, eliminar, tokenizados_seg)
            break

        print(INPUT_INVALIDO)
    return diccionario, tokenizados_seg


def validar_ids(eliminar, busqueda):
    """recibe un set y los resultados de busqueda.

    verifica que el set no este vacio y que sus elementos pertenezcan
    a la busqueda."""

    if not eliminar:
        return False
    for id in eliminar:
        if id not in busqueda:
            return False
    return True


def ids_a_eliminar(ingreso):
    """recibe el input del usuario, separa dependiendo de que sea un
    rango o un numero solo y actualiza los valores de los indices en
    el set ya creado."""

    eliminar = set()
    para_eliminar = ingreso.split(",")
    for elemento in para_eliminar:
        elemento = elemento.strip()
        if "-" in elemento:
            eliminar_rango(elemento, eliminar)
        elif elemento.isdigit():
            eliminar_directo(elemento, eliminar)
    return eliminar


def eliminar_rango(elemento, eliminar):
    """recibe strings y el set que contiene los indices a eliminar
    verifica que sean caracteres validos y añade dichos indices a eliminar,
    en caso contrario devuelve input invalido."""

    rango = elemento.split("-")
    desde, hasta = rango
    if desde.isnumeric() and hasta.isnumeric():
        desde, hasta = map(int, rango)
        for indice in range(desde, hasta + 1):
            eliminar.add(indice)
    else:
        print(INPUT_INVALIDO)
    return eliminar


def eliminar_directo(elemento, eliminar):
    """recibe una string y el set que contiene los indices a eliminar
    verifica el elemento string sea un numero y lo añade al set, en caso
    contrario devuelve input invalido."""

    if elemento.isdigit():
        indice = int(elemento)
        eliminar.add(indice)
    else:
        print(INPUT_INVALIDO)
    return eliminar


def eliminar_claves(diccionario, busqueda, eliminar, tokenizados_seg):
    """recibe el diccionario con los tweets creados, los resultados
    de busqueda, el set que contiene los indices a eliminar y
    el diccionario con los tweets ya tokenizados.

    verifica que los elementos del set esten en la busqueda y en el diccionario
    y los agrega a otro set para posteriormente mostrar por pantalla
    los tweets eliminados y eliminar los mismos tanto del diccionario
    de tweets como sus tokenizaciones."""

    eliminados = set()
    for id in eliminar:
        if id in busqueda and id in diccionario:
            eliminados.add(id)

    if not eliminados:
        print(INPUT_INVALIDO)
    else:
        print(TWEETS_ELIMINADOS)
        for id in eliminados:
            print(f"{id}.", diccionario[id])
            diccionario.pop(id)
        eliminar_tokenizaciones(eliminados, tokenizados_seg)


def tokenizacion_por_segmento(texto):
    """recibe una string y tokeniza por segmentos de n>=3, eliminando
    caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    texto = str(texto).lower()
    for char in texto:
        if not char.isalnum():
            texto = texto.replace(char, " ")
    palabras = texto.split(" ")
    tokenizacion = []
    for palabra in palabras:
        for i in range(len(palabra)):
            for j in range(i + 2, len(palabra)):
                token = texto[i : j + 1]
                tokenizacion.append(token)
    return tokenizacion


def tokenizacion_simple(texto):
    """recibe una string y la tokeniza por palabras, separadas por
    espacios, elimina caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    palabras = []
    texto = str(texto).lower()
    for letra in texto:
        if not letra.isalnum():
            texto = texto.replace(letra, " ")
    palabras = texto.strip().split()
    return palabras


def tokenizacion_completa(texto):
    """recibe una string y realiza los dos tipos de tokenizaciones
    de la misma.

    devuelve dos listas con las tokenizaciones respectivas."""
    palabra = tokenizacion_simple(texto)
    segmento = tokenizacion_por_segmento(texto)
    return palabra, segmento


def agregar_tokenizacion(tokenizados_seg, id, ingreso):
    """agrega los dos tipos de tokenizaciones de un string a un mismo
    diccionario, guardando los ids en un mismo set por cada clave,
    teniendo en cuenta los casos en que la palabra tiene menos de
    tres caracteres.

    devuelve el diccionario de las tokenizaciones."""
    tokenizacion_pal, tokenizacion_segmento = tokenizacion_completa(ingreso)

    for token in tokenizacion_segmento:
        tokenizados_seg[token] = tokenizados_seg.get(token, set())
        tokenizados_seg[token].add(id)

    for token in tokenizacion_pal:
        tokenizados_seg[token] = tokenizados_seg.get(token, set())
        tokenizados_seg[token].add(id)
    return tokenizados_seg


def eliminar_tokenizaciones(eliminar, diccionario):
    """recibe el set con los ids para eliminar y el diccionario de las
    tokenizaciones.

    elimina del diccionario aquellos tokens que contengan algun id en
    sus valores, devuelve el diccionario modificado."""

    claves_a_borrar = set()
    for clave, listas in diccionario.items():
        for id in eliminar:
            if id in listas:
                claves_a_borrar.add(clave)

    for clave in claves_a_borrar:
        diccionario.pop(clave)

    return diccionario
