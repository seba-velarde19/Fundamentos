from algo_twitter2 import (
    crear_tweet,
    buscar_tweet,
    eliminar_tweet,
    normalizar,
    BUSQUEDA,
    ELIMINAR,
)

INPUT_INVALIDO = "Input invalido."


def main():
    tweets_existentes = []
    id = 0
    while True:
        print()
        mostrar_inicio()
        ingreso = input("")
        if ingreso == "1":
            tweets_existentes, id = crear_tweet(tweets_existentes, id)
        elif ingreso == "2":
            buscar_tweet(tweets_existentes, BUSQUEDA)
        elif ingreso == "3":
            eliminar_tweet(tweets_existentes)
        elif ingreso == "4":
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


def mostrar_inicio():
    # con input
    print("1. Crear Tweet")
    print("2. Buscar Tweet")
    print("3. Eliminar Tweet")
    print("4. Salir")


main()
