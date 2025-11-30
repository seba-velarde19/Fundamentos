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
ELEGIR_OPCION = "1. Crear Tweet\n2. Buscar Tweet\n3. Eliminar Tweet\n4. Salir\n"
INDICE_A_ELIMINAR = "Ingrese el numero de tweet que quiere eliminar:\n"
SELECCION = "Seleccione una de las opciones:\n\n"


def main():
    """ejecuta el programa principal, entrando a cada funcion dependiendo de
    la eleccion del usuario"""

    tweets_existentes = {}
    id = 0
    tokenizados_seg = {}
    while True:
        ingreso = mostrar_inicio()
        if ingreso == OPCION_CREAR_TWEET:
            tweets_existentes, id, tokenizados_seg = crear_tweet(
                tweets_existentes, id, tokenizados_seg
            )
        elif ingreso == OPCION_BUSCAR_TWEET:
            buscar_tweet(tweets_existentes, tokenizados_seg, BUSCAR)
        elif ingreso == OPCION_ELIMINAR_TWEET:
            eliminar_tweet(tweets_existentes, tokenizados_seg, ELIMINAR)
        elif ingreso == OPCION_SALIR:
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


def mostrar_inicio():
    """muestra al usuario las opciones del programa y guarda el
    valor ingresado"""

    ingreso = input(f"\n{SELECCION}{ELEGIR_OPCION}>>> ")
    return ingreso


def crear_tweet(tweets_existentes, id, tokenizados_seg):
    """recibe diccionario con los tweets ya creados, el numero
    de id que corresponde y el diccionario con los tweets tokenizados.

    le pide al usuario el ingreso de un tweet, lo tokeniza y guarda
    en diccionarios distintos, uno para los tweets y
    otro para las tokenizaciones despues imprime por
    pantalla el numero de tweet guardado y devuelve los
    diccionarios actualizados."""
    while True:
        ingreso = input("Ingrese un tweet a almacenar:\n>>> ")
        if ingreso == ATRAS:
            return tweets_existentes, id, tokenizados_seg
        if ingreso == "" or tokenizacion_simple(ingreso) == []:
            print(INPUT_INVALIDO)
        else:
            break
    tokenizados_seg = agregar_tokenizacion(tokenizados_seg, id, ingreso)
    tweet = ingreso
    tweets_existentes[id] = tweet
    print(f"OK {id}")
    id += 1
    return tweets_existentes, id, tokenizados_seg


def buscar_tweet(diccionario, tokenizados_seg, mensaje):
    """recibe el diccionario de tweets existentes y el diccionario de
    las tokenizaciones.

    le pide al usuario el ingreso de palabras a buscar y las tokeniza
    para despues recorrer estas tokenizaciones y analizar la existencia
    de todos los tokens en el diccionario de los tweets tokenizados,
    en el caso de encontrarlos los agrega a un set
    para posteriormente imprimir los tweets encontrados
    junto con sus ids correspondientes."""

    while True:
        palabras_clave = input(f"{mensaje}")
        if palabras_clave == ATRAS:
            return diccionario, palabras_clave

        tokens_input = tokenizacion_simple(palabras_clave)

        if not tokens_input:
            print(INPUT_INVALIDO)
            continue

        listas_ids = obtener_ids_coincidentes(tokens_input, tokenizados_seg)
        resultado = set.intersection(*listas_ids)

        if not resultado:
            print(NO_ENCONTRADOS)
            return resultado, palabras_clave

        print(RESULTADOS_BUSQUEDA)
        for id in sorted(resultado):
            print(f"{id}. {diccionario[id]}")
        break

    return resultado, palabras_clave


def eliminar_tweet(diccionario, tokenizados_seg, mensaje):
    """recibe el diccionario de los tweets existentes y las tokenizaciones de
    los tweets.

    realiza una busqueda para saber que es lo que se busca eliminar,
    si la busqueda no es vacia muestra lo encontrado y le
    pide al usuario el ingreso del indice a eliminar,
    en el caso de que el indice exista se elimina el/los tweets
    y se muestran por pantalla, en el caso contrario
    se muestra un mensaje de numero invalido o no encontrados
    correspondientemente"""

    eliminar = set()
    busqueda, palabras_clave = buscar_tweet(diccionario, tokenizados_seg, mensaje)
    if not busqueda or palabras_clave == ATRAS:
        return diccionario, tokenizados_seg, mensaje
    while True:
        ingreso_a_eliminar = input(f"{INDICE_A_ELIMINAR}>>> ")
        if ingreso_a_eliminar == ATRAS:
            return diccionario, tokenizados_seg
        eliminar, validar_rango = ids_a_eliminar(ingreso_a_eliminar)
        if validar_rango != "":
            print(validar_rango)
            continue
        validacion, mensaje = validar_ids(eliminar, busqueda)
        if validacion:
            eliminar_claves(diccionario, busqueda, eliminar, tokenizados_seg)
            break
        if not validacion:
            print(mensaje)
        if not validacion and mensaje == NO_ENCONTRADOS:
            return diccionario, tokenizados_seg

    return diccionario, tokenizados_seg


def obtener_ids_coincidentes(tokens_input, tokenizados_seg):
    """se encarga de encontrar todos los tokens que coincidan con
    lo ingresado y eso lo guarda en una lista para usar en la funcion
    principal"""

    listas_ids = []
    for token in tokens_input:
        ids = set()
        for token_guardado in tokenizados_seg:
            if token == token_guardado:
                ids.update(tokenizados_seg[token_guardado])
        listas_ids.append(ids)
    return listas_ids


def validar_ids(eliminar, busqueda):
    """recibe un set y los resultados de busqueda.

    verifica que el set no este vacio y que sus elementos pertenezcan
    a la busqueda."""
    no_encontrado = 0
    if not eliminar:
        return False, INPUT_INVALIDO
    for id in eliminar:
        if id not in busqueda:
            no_encontrado += 1
    if no_encontrado > 0 and len(eliminar) > 1:
        return False, NUMERO_INVALIDO
    if no_encontrado > 0:
        return False, NO_ENCONTRADOS
    return True, ""


def ids_a_eliminar(ingreso):
    """recibe el input del usuario, separa dependiendo de que sea un
    rango o un numero solo y actualiza los valores de los indices en
    el set ya creado."""

    eliminar = set()
    para_eliminar = ingreso.split(",")
    mensaje = ""

    if ingreso.strip() == "":
        return eliminar, INPUT_INVALIDO

    for elemento in para_eliminar:
        elemento = elemento.strip()
        if "-" in elemento:
            eliminar, mensaje = eliminar_rango(elemento, eliminar)
            if mensaje != "":
                return eliminar, mensaje
        elif elemento.isdigit():
            eliminar_directo(elemento, eliminar)
        else:
            return (
                eliminar,
                INPUT_INVALIDO,
            )

    return eliminar, mensaje


def eliminar_rango(elemento, eliminar):
    """recibe strings y el set que contiene los indices a eliminar
    verifica que sean caracteres validos y añade dichos indices a eliminar,
    en caso contrario devuelve input invalido."""

    while True:
        rango = elemento.split("-")
        mensaje = ""
        if len(rango) > 2:
            mensaje = INPUT_INVALIDO
            return eliminar, mensaje

        desde, hasta = rango[0].strip(), rango[1].strip()
        if not (desde.isnumeric() and hasta.isnumeric()):
            mensaje = INPUT_INVALIDO
            return eliminar, mensaje

        desde, hasta = int(desde), int(hasta)
        if desde > hasta:
            mensaje = INPUT_INVALIDO
            return eliminar, mensaje

        for indice in range(desde, hasta + 1):
            eliminar.add(indice)
        break

    return eliminar, mensaje


def eliminar_directo(elemento, eliminar):
    """recibe una string y el set que contiene los indices a eliminar
    y añade el numero."""

    indice = int(elemento)
    eliminar.add(indice)
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
        print(NUMERO_INVALIDO)
        return eliminar

    print(TWEETS_ELIMINADOS)
    for id in eliminados:
        print(f"{id}. {diccionario[id]}")
        diccionario.pop(id)
    eliminar_tokenizaciones(eliminados, tokenizados_seg)
    return eliminar


def tokenizacion_por_segmento(texto):
    """recibe una string y tokeniza por segmentos de n>=3, eliminando
    caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    texto = sacar_tildes_dieresis(str(texto).lower())
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


def tokenizacion_simple(texto):
    """recibe una string y la tokeniza por palabras, separadas por
    espacios, elimina caracteres especiales y mayusculas.

    devuelve una lista con las tokenizaciones."""

    texto = sacar_tildes_dieresis(str(texto).lower())
    texto_nuevo = ""
    for letra in texto:
        if not letra.isalnum():
            texto_nuevo += " "
        else:
            texto_nuevo += letra
    texto = " ".join(texto_nuevo.split())
    palabras = texto.split()
    return palabras


def tokenizacion_completa(texto):
    """recibe una string y realiza los dos tipos de tokenizaciones
    de la misma.

    devuelve dos listas con las tokenizaciones respectivas."""
    palabra = tokenizacion_simple(texto)
    segmento = tokenizacion_por_segmento(texto)
    return palabra, segmento


def sacar_tildes_dieresis(texto):
    """Reemplaza letras con tilde y dieresis por su equivalente sin tilde, usando .get()."""
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

    claves_a_eliminar = []

    for token, ids in diccionario.items():
        for id in list(eliminar):
            if id in ids:
                ids.remove(id)
        if not ids:
            claves_a_eliminar.append(token)

    for clave in claves_a_eliminar:
        diccionario.pop(clave)

    return diccionario


if __name__ == "__main__":
    main()
