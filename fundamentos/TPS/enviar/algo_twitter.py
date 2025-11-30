import funciones as f

FIN = "Finalizando..."
INPUT_INVALIDO = "Input invalido."


def main():
    tweets_existentes = {}
    id = 0
    while True:
        ingreso = f.mostrar_inicio()
        if ingreso == "1":
            tweets_existentes, id = f.crear_tweet(tweets_existentes, id)
        elif ingreso == "2":
            f.buscar_tweet(tweets_existentes)
        elif ingreso == "3":
            f.eliminar_tweet(tweets_existentes)
        elif ingreso == "4":
            print(FIN)
            break
        else:
            print(INPUT_INVALIDO)


main()
