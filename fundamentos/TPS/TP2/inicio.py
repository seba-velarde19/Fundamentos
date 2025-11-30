from algo_twitter import crear_tweet, buscar_tweet, eliminar_tweet, normalizar

NUMERO_INVALIDO = "Numero de tweet invalido."
NO_ENCONTRADOS = "No se encontraron tweets."
INPUT_INVALIDO = "Input invalido."
FIN = "Finalizando..."
RESULTADOS_BUSQUEDA = "Resultados de la busqueda:"
TWEETS_ELIMINADOS = "Tweets eliminados:"
ATRAS = "**"


def main():
    original = []
    tweets_existentes = []
    id = 0
    while True:
        print()
        mostrar_inicio()
        ingreso = input("")
        if ingreso == "1":
            tweets_existentes, id, original = crear_tweet(
                tweets_existentes, id, original
            )
        elif ingreso == "2":
            buscar_tweet(original)
        elif ingreso == "3":
            eliminar_tweet(original)
        elif ingreso == "4":
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


def mostrar_inicio():
    print("1. Crear Tweet")
    print("2. Buscar Tweet")
    print("3. Eliminar Tweet")
    print("4. Salir")


main()
