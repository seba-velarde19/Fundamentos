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
OPCION_SALIR = "4"
ELEGIR_OPCION = "1. Crear Tweet\n2. Buscar Tweet\n3. Eliminar Tweet\n4. Salir\n>>> "
INDICE_A_ELIMINAR = "Ingrese el numero de tweet que quiere eliminar:\n>>> "
SELECCION = "\nSeleccione una de las opciones:\n\n"
INGRESO_CREACION = "Ingrese un tweet a almacenar:\n>>> "


def main():
    """ejecuta el programa principal, entrando a cada funcion dependiendo de
    la eleccion del usuario"""

    tweets_existentes = {}
    id = 0
    tokenizados_existentes = {}
    inverso_tokenizados = {}
    while True:
        ingreso = mostrar_inicio()
        if ingreso == OPCION_CREAR_TWEET:
            id = crear_tweet(
                tweets_existentes, id, tokenizados_existentes, inverso_tokenizados
            )
        elif ingreso == OPCION_BUSCAR_TWEET:
            buscar_tweet(tweets_existentes, tokenizados_existentes, BUSCAR)
        elif ingreso == OPCION_ELIMINAR_TWEET:
            eliminar_tweet(
                tweets_existentes, tokenizados_existentes, inverso_tokenizados, ELIMINAR
            )
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


def crear_tweet(tweets_existentes, id, tokenizados_existentes, inverso_tokens):
    """recibe diccionario con los tweets ya creados, el numero
    de id que corresponde y el diccionario con los tweets tokenizados.

    tokeniza el ingreso y lo guarda
    en diccionarios distintos, uno para los tweets y otros dos
    para las tokenizaciones despues imprime por pantalla
    el numero de tweet guardado"""

    validacion, ingreso = verificar_ingreso(INGRESO_CREACION)
    if validacion:
        agregar_tokenizacion(tokenizados_existentes, inverso_tokens, id, ingreso)
        tweets_existentes[id] = ingreso
        print(f"OK {id}")
        id += 1
    return id


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


def tokenizar_por_segmento(texto):
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
            for j in range(i + 2, len(palabra)):
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


def tokenizar_completo(texto):
    """recibe una string y realiza los dos tipos de tokenizaciones
    de la misma.

    devuelve dos listas con las tokenizaciones respectivas."""
    palabra = tokenizar_simple(texto)
    segmento = tokenizar_por_segmento(texto)
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


def agregar_tokenizacion(tokenizados_existentes, inverso_tokens, id, ingreso):
    """agrega los dos tipos de tokenizaciones de un string a un mismo
    diccionario, guardando los ids en un mismo set por cada clave,
    teniendo en cuenta los casos en que la palabra tiene menos de
    tres caracteres, ademas guarda los mismo valores de forma
    inversa para utilizar de forma mas eficiente mas adelante."""

    tokenizacion_pal, tokenizacion_segmento = tokenizar_completo(ingreso)
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
    main()
