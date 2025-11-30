def validar_contrasena(numero):
    contrasena = input("ingrese contrasena: ")
    letras = []
    numeros = []
    especiales = []
    intentos = int(numero)
    for letra in contrasena:
        if not letra.isalnum():
            especiales.append(letra)
        elif not letra.isalpha():
            numeros.append(letra)
        else:
            letras.append(letra)

    while intentos >= 0:
        if len(numeros) < 2:
            print(f"te quedan {intentos} intentos")
            print("debe tener 2 numeros o mas")
            intentos -= 1
            validar_contrasena(intentos)
        elif len(letras) < len(numeros):
            print(f"te quedan {intentos} intentos")
            print("no podes tener mas numeros que letras")
            intentos -= 1
            validar_contrasena(intentos)
        elif len(especiales) == 0 or len(especiales) > 3:
            print(f"te quedan {intentos} intentos")
            print("debes tener entre uno y 3 caracteres especiales")
            intentos -= 1
            validar_contrasena(intentos)
        else:
            print("contrasena creada")
            intentos = 0
            # por que break no funciona?
            # por que se pasa
    print(f"se terminaron los intentos({intentos})")


validar_contrasena(10)
