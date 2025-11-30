def primera_mayuscula():
    lista_nombres = []
    for i in range(5):
        nombre = input(f"ingresa el nombre {i+1}: ").capitalize()
        lista_nombres.append(nombre)
    lista_nueva = ",".join(lista_nombres)
    return lista_nueva


primera_mayuscula()
