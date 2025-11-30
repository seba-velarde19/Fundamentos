contraseña = input("ingrese una contrasena: ")

while True:
    ingreso = input("contrasena: ")
    if ingreso != contraseña:
        print("contrasena incorrecta")
    else:
        print("acceso concedido")
        break
