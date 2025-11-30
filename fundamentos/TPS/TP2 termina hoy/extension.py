def eliminar_tweet(diccionario, tokenizados_pal, tokenizados_seg):
    a_eliminar=set()
    busqueda = buscar_tweet(diccionario, tokenizados_pal, tokenizados_seg)
    ingreso_a_eliminar = input("Ingrese el numero de tweet que quiere eliminar:\n")
    if ingreso_a_eliminar == ATRAS:
        return diccionario
    para_eliminar = ingreso_a_eliminar.split(",")
    for elemento in para_eliminar:
        elemento = elemento.strip()
        if "-" in elemento:
            eliminar_rangos=eliminacion_por_rango(elemento,busqueda)
        elif elemento.isdigit():
            eliminar_indice=eliminacion_directa(elemento,busqueda)
    eliminar_claves(diccionario,a_eliminar,eliminar_rangos,eliminar_indice)

def eliminacion_por_rango(elemento, busqueda):
    eliminar_rango=[]
    rango = elemento.split("-")
    desde, hasta = rango
    if desde.isnumeric() and hasta.isnumeric():
        desde, hasta = map(int, rango)

        for indice in range(desde, hasta + 1):
           eliminar_rango.append(indice)

    else:
        print(INPUT_INVALIDO)

    return eliminar_rango


def eliminacion_directa(elemento, busqueda):
    eliminar_directo = []
    if elemento.isdigit():
        indice = int(elemento)
        eliminar_directo.append(indice)
    else:
        print(INPUT_INVALIDO)
    return eliminar_directo


def eliminar_claves(diccionario,a_eliminar,eliminar_rangos,eliminar_indice):
    eliminar_rangos.extend(eliminar_indice)
    eliminar_rangos.sort()
    a_eliminar.update(eliminar_rangos)
    if not a_eliminar:
        print(INPUT_INVALIDO)
    else:
        for item in a_eliminar:
            if item in diccionario:
                diccionario.pop(item)
    return diccionario

def agregar_tokenizacion(tokenizados_pal,tokenizados_seg,id):
    tokenizacion_palabra,tokenizacion_segmento=tokenizacion_completa(ingreso):
    if tokenizacion_palabra == []:
        print(INPUT_INVALIDO)
        return tokenizados_pal,tokenizados_seg
    if not tokenizacion_palabra in tokenizados_pal:
        tokenizados_pal[tokenizacion_palabra]=[]
        tokenizados_pal[tokenizacion_palabra].append(id)
    else:
        tokenizados_pal[tokenizacion_palabra].append(id)

     for token in tokenizacion_seg:
        if not token in tokenizados_seg:
            tokenizados_seg[token] = []
            tokenizados_seg.append(id)
        else:
            tokenizados_seg[token].append(id)
    return tokenizados_pal,tokenizados_seg

def eliminar_tokenizaciones(id,resultado,diccionario):
    for clave,listas in diccionario.items():
        if id in listas:
            diccionario.pop[clave]
    return diccionario