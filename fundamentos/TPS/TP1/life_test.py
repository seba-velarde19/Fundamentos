import pprint
import sys
import traceback

import life

# Si las pruebas se ven mal en tu terminal, probá cambiando el valor
# de esta constante a True para desactivar los colores ANSI.
TERMINAL_SIN_COLOR = False


def generar_mensaje_error(esperado, obtenido):
    """Genera un mensaje de error estándar para las pruebas."""
    error_msg = "Estado esperado:\n"
    error_msg += pprint.pformat(esperado) + "\n"
    error_msg += "\n"
    error_msg += "Estado actual:\n"
    error_msg += pprint.pformat(obtenido) + "\n"
    return error_msg


def test_00_crear_vacio():
    """Valida la creación de un tablero vacío"""
    inicial = []
    tablero = life.life_crear(inicial)
    try:
        assert tablero == []
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error([], tablero)) from exc


def test_01_crear_con_un_elemento_false():
    """Valida la creación de un tablero con un solo elemento False"""
    inicial = ["."]
    tablero = life.life_crear(inicial)
    try:
        assert tablero == [[False]]
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error([[False]], tablero)) from exc


def test_02_crear_con_un_elemento_true():
    """Valida la creación de un tablero con un solo elemento True"""
    inicial = ["#"]
    tablero = life.life_crear(inicial)
    try:
        assert tablero == [[True]]
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error([[True]], tablero)) from exc


def test_03_crear_con_dos_elementos():
    """Valida la creación de un tablero con dos elementos"""
    inicial = ["#.", ".#"]
    tablero = life.life_crear(inicial)
    try:
        assert tablero == [[True, False], [False, True]]
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error([[True, False], [False, True]], tablero)
        ) from exc


def test_04_mostrar_tablero_vacio():
    """Valida que `life_mostrar` muestre un tablero vacío correctamente"""
    inicial = []
    tablero = life.life_mostrar(inicial)
    try:
        assert tablero == []
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error([], tablero)) from exc


def test_05_mostrar_tablero_con_un_elemento_false():
    """Valida que `life_mostrar` muestre un tablero con un solo elemento False"""
    inicial = [[False]]
    tablero = life.life_mostrar(inicial)
    try:
        assert tablero == ["."]
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(["."], tablero)) from exc


def test_06_mostrar_tablero_con_un_elemento_true():
    """Valida que `life_mostrar` muestre un tablero con un solo elemento True"""
    inicial = [[True]]
    tablero = life.life_mostrar(inicial)
    try:
        assert tablero == ["#"]
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(["#"], tablero)) from exc


def test_07_mostrar_tablero_con_dos_elementos():
    """Valida que `life_mostrar` muestre un tablero de 2x2"""
    inicial = [[True, False], [False, True]]
    tablero = life.life_mostrar(inicial)
    try:
        assert tablero == ["#.", ".#"]
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(["#.", ".#"], tablero)) from exc


def test_08_cant_adyacentes_con_tablero_un_elemento():
    """Valida que la cantidad de adyacentes de un tablero con un solo elemento en la posición especificada sea 0"""
    inicial = life.life_crear(["."])
    cantidad = life.cant_adyacentes(inicial, 0, 0)
    try:
        assert cantidad == 0
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(0, cantidad)) from exc


def test_09_cant_adyacentes_dos_x_dos_1():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 0"""
    inicial = life.life_crear(["..", ".."])
    cantidad = life.cant_adyacentes(inicial, 0, 0)
    try:
        assert cantidad == 0
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(0, cantidad)) from exc


def test_10_cant_adyacentes_dos_x_dos_2():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 0"""
    inicial = life.life_crear(["..", ".."])
    cantidad = life.cant_adyacentes(inicial, 0, 1)
    try:
        assert cantidad == 0
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(0, cantidad)) from exc


def test_11_cant_adyacentes_dos_x_dos_3():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 2"""
    inicial = life.life_crear(["##", ".."])
    cantidad = life.cant_adyacentes(inicial, 0, 0)
    try:
        assert cantidad == 2
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(2, cantidad)) from exc


def test_12_cant_adyacentes_dos_x_dos_4():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 2"""
    inicial = life.life_crear(["##", ".."])
    cantidad = life.cant_adyacentes(inicial, 0, 1)
    try:
        assert cantidad == 2
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(2, cantidad)) from exc


def test_13_cant_adyacentes_dos_x_dos_5():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 4"""
    inicial = life.life_crear(["#.", ".#"])
    cantidad = life.cant_adyacentes(inicial, 0, 0)
    try:
        assert cantidad == 4
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(4, cantidad)) from exc


def test_14_cant_adyacentes_dos_x_dos_6():
    """Valida que la cantidad de adyacentes de un tablero de 2x2 en la posición especificada sea 8"""
    inicial = life.life_crear(["##", "##"])
    cantidad = life.cant_adyacentes(inicial, 0, 0)
    try:
        assert cantidad == 8
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(8, cantidad)) from exc


def test_15_cant_adyacentes_tres_x_tres_1():
    """Valida que la cantidad de adyacentes de un tablero de 3x3 en la posición especificada sea 4"""
    inicial = life.life_crear([".#.", "#.#", ".#."])
    cantidad = life.cant_adyacentes(inicial, 1, 1)
    try:
        assert cantidad == 4
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                4,
                cantidad,
            )
        ) from exc


def test_16_cant_adyacentes_tres_x_tres_2():
    """Valida que la cantidad de adyacentes de un tablero de 3x3 en la posición especificada sea 3"""
    inicial = life.life_crear([".#.", "..#", ".#."])
    cantidad = life.cant_adyacentes(inicial, 1, 1)
    try:
        assert cantidad == 3
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                3,
                cantidad,
            )
        ) from exc


def test_17_cant_adyacentes_tres_x_tres_3():
    """Valida que la cantidad de adyacentes de un tablero de 3x3 en la posición especificada sea 0"""
    inicial = life.life_crear(["...", ".#.", "..."])
    cantidad = life.cant_adyacentes(inicial, 1, 1)
    try:
        assert cantidad == 0
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                0,
                cantidad,
            )
        ) from exc


def test_18_celda_siguiente_un_elemento():
    """Valida que el siguiente estado en una celda específica de un tablero con un posición especificada sea False"""
    inicial = life.life_crear(["."])
    resultado = life.celda_siguiente(inicial, 0, 0)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(False, resultado)) from exc


def test_19_celda_siguiente_dos_x_dos_1():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea False"""
    inicial = life.life_crear(["..", ".."])
    resultado = life.celda_siguiente(inicial, 0, 0)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(False, resultado)) from exc


def test_20_celda_siguiente_dos_x_dos_2():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea False"""
    inicial = life.life_crear(["..", ".."])
    resultado = life.celda_siguiente(inicial, 0, 1)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(False, resultado)) from exc


def test_21_celda_siguiente_dos_x_dos_3():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea True"""
    inicial = life.life_crear(["##", ".."])
    resultado = life.celda_siguiente(inicial, 0, 0)
    try:
        assert resultado == True
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(True, resultado)) from exc


def test_22_celda_siguiente_dos_x_dos_4():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea True"""
    inicial = life.life_crear(["##", ".."])
    resultado = life.celda_siguiente(inicial, 0, 1)
    try:
        assert resultado == True
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(True, resultado)) from exc


def test_23_celda_siguiente_dos_x_dos_5():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea False"""
    inicial = life.life_crear(["#.", ".#"])
    resultado = life.celda_siguiente(inicial, 0, 0)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(False, resultado)) from exc


def test_24_celda_siguiente_dos_x_dos_6():
    """Valida que el siguiente estado en una celda específica de un tablero de 2x2 sea False"""
    inicial = life.life_crear(["##", "##"])
    resultado = life.celda_siguiente(inicial, 0, 0)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(generar_mensaje_error(False, resultado)) from exc


def test_25_celda_siguiente_tres_x_tres_1():
    """Valida que el siguiente estado en una celda específica de un tablero de 3x3 sea False"""
    inicial = life.life_crear([".#.", "#.#", ".#."])
    resultado = life.celda_siguiente(inicial, 1, 1)
    try:
        assert resultado == False
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                False,
                resultado,
            )
        ) from exc


def test_26_celda_siguiente_tres_x_tres_2():
    """Valida que el siguiente estado en una celda específica de un tablero de 3x3 sea True"""
    inicial = life.life_crear([".#.", "..#", ".#."])
    resultado = life.celda_siguiente(inicial, 1, 1)
    try:
        assert resultado == True
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                True,
                resultado,
            )
        ) from exc


def test_27_cant_adyacentes_tres_x_tres_4():
    """Valida que la cantidad de adyacentes de un tablero de 3x3 en la posición especificada sea 0"""
    inicial = life.life_crear(["...", ".#.", "..."])
    cantidad = life.cant_adyacentes(inicial, 1, 1)
    try:
        assert cantidad == 0
    except AssertionError as exc:
        raise AssertionError(
            generar_mensaje_error(
                0,
                cantidad,
            )
        ) from exc


# Sólo se van a correr aquellos tests que estén mencionados dentro de la
# siguiente constante
TESTS = (
    test_00_crear_vacio,
    test_01_crear_con_un_elemento_false,
    test_02_crear_con_un_elemento_true,
    test_03_crear_con_dos_elementos,
    test_04_mostrar_tablero_vacio,
    test_05_mostrar_tablero_con_un_elemento_false,
    test_06_mostrar_tablero_con_un_elemento_true,
    test_07_mostrar_tablero_con_dos_elementos,
    test_08_cant_adyacentes_con_tablero_un_elemento,
    test_09_cant_adyacentes_dos_x_dos_1,
    test_10_cant_adyacentes_dos_x_dos_2,
    test_11_cant_adyacentes_dos_x_dos_3,
    test_12_cant_adyacentes_dos_x_dos_4,
    test_13_cant_adyacentes_dos_x_dos_5,
    test_14_cant_adyacentes_dos_x_dos_6,
    test_15_cant_adyacentes_tres_x_tres_1,
    test_16_cant_adyacentes_tres_x_tres_2,
    test_17_cant_adyacentes_tres_x_tres_3,
    test_18_celda_siguiente_un_elemento,
    test_19_celda_siguiente_dos_x_dos_1,
    test_20_celda_siguiente_dos_x_dos_2,
    test_21_celda_siguiente_dos_x_dos_3,
    test_22_celda_siguiente_dos_x_dos_4,
    test_23_celda_siguiente_dos_x_dos_5,
    test_24_celda_siguiente_dos_x_dos_6,
    test_25_celda_siguiente_tres_x_tres_1,
    test_26_celda_siguiente_tres_x_tres_2,
    test_27_cant_adyacentes_tres_x_tres_4,
)

# El código que viene abajo tiene algunas *magias* para simplificar la corrida
# de los tests y proveer la mayor información posible sobre los errores que se
# produzcan. ¡No te preocupes si no lo entendés completamente!

# Colores ANSI para una salida más agradable en las terminales que lo permitan
COLOR_OK = "\033[1m\033[92m"
COLOR_ERR = "\033[1m\033[91m"
COLOR_RESET = "\033[0m"


def print_color(color: str, *args, **kwargs):
    """
    Mismo comportamiento que `print` pero con un
    primer parámetro para indicar de qué color se
    imprimirá el texto.

    Si la constante TERMINAL_SIN_COLOR es True,
    esta función será exactamente equivalente
    a utilizar `print`.
    """
    if TERMINAL_SIN_COLOR:
        print(*args, **kwargs)
    else:
        print(color, end="")
        print(*args, **kwargs)
        print(COLOR_RESET, end="", flush=True)


def main():
    tests_fallidos = []
    tests_a_correr = [int(t) for t in sys.argv[1:]]
    for i, test in [
        (i, test)
        for i, test in enumerate(TESTS)
        if not tests_a_correr or i + 1 in tests_a_correr
    ]:
        print(f"Prueba {i + 1 :02} - {test.__name__}: ", end="", flush=True)
        try:
            test()
            print_color(COLOR_OK, "[OK]")
        except AssertionError as e:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[ERROR]")
            print_color(COLOR_ERR, " >", *e.args)
            break
        except Exception:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[BOOM - Explotó]")
            print("\n--------------- Python dijo: ---------------")
            traceback.print_exc()
            print("--------------------------------------------\n")
            break

    if not tests_fallidos:
        print()
        print_color(COLOR_OK, "###########")
        print_color(COLOR_OK, "# TODO OK #")
        print_color(COLOR_OK, "###########")
        print()
    else:
        print()
        print_color(COLOR_ERR, "##################################")
        print_color(COLOR_ERR, "              ¡ERROR!             ")
        print_color(COLOR_ERR, "Falló el siguiente test:")
        for test_con_error in tests_fallidos:
            print_color(COLOR_ERR, " - " + test_con_error)
        print_color(COLOR_ERR, "##################################")
        print(
            "TIP: Si la información de arriba no es suficiente para entender "
            "el error, revisá el código de las pruebas que fallaron en el "
            "archivo life.test.py."
        )


main()
