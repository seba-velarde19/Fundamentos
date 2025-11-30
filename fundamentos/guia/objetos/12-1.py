class intervalo:
    def __init__(self, desde, hasta):
        if desde >= hasta:
            raise ValueError("Desde debe ser menos que hasta")
        self.desde = desde
        self.hasta = hasta

    def duracion(self):
        tiempo = self.hasta - self.desde
        return tiempo

    def interseccion(self, otro):
        if not isinstance(otro, intervalo):
            raise TypeError("no es de tipo intervalo")
        nuevo_desde = max(self.desde, otro.desde)
        nuevo_hasta = min(self.hasta, otro.hasta)
        if nuevo_desde >= nuevo_hasta:
            raise ValueError("no se intersectan")
        return intervalo(nuevo_desde, nuevo_hasta)

    def union(self, otro):
        if not isinstance(otro, intervalo):
            raise TypeError("no es de tipo intervalo")
        intersectan = max(self.desde, otro.desde) < min(self.hasta, otro.hasta)
        adyacente = self.hasta == otro.desde or self.desde == otro.hasta
        if not intersectan or not adyacente:
            raise ValueError("no se intersectan")
        nuevo_desde = min(self.desde, otro.desde)
        nuevo_hasta = max(self.hasta, otro.hasta)
        return intervalo(nuevo_desde, nuevo_hasta)


def simplificar_(self, clase):
    if self.dividendo % 2 == 0 and self.divisor % 2 == 0:
        nuevo = clase(self.dividendo // 2, self.divisor // 2)
        return simplificar_(nuevo, clase)
    return clase(self.dividendo, self.divisor)


class Fraccion:
    def __init__(self, dividendo, divisor):
        if divisor == 0:
            raise ValueError("no se puede dividir por 0")
        self.dividendo = dividendo
        self.divisor = divisor

    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"

    def __add__(self, otro):
        if not isinstance(otro, Fraccion):
            raise TypeError("no es de tipo fraccion")
        divisor = self.divisor * otro.divisor
        dividendo = (self.dividendo * otro.divisor) + (otro.dividendo * self.divisor)
        return Fraccion(dividendo, divisor)

    def __mul__(self, otro):
        if not isinstance(otro, Fraccion):
            raise TypeError("no es de tipo fraccion")
        dividendo = self.dividendo * otro.dividendo
        divisor = self.divisor * otro.divisor
        return Fraccion(dividendo, divisor)

    def simplificar(self):
        return simplificar_(self, Fraccion)


class Vector:
    def __init__(self, coord):
        if not isinstance(coord, list):
            raise TypeError("El argumento debe ser una lista de n caracteres")
        self.coord = coord

    def __str__(self):
        return f"{self.coord}"

    def __add__(self, otro):
        if not isinstance(otro, Vector):
            raise TypeError("no es de tipo vector")
        if len(self.coord) != len(otro.coord):
            raise ValueError("los vectores son de diferente longitud")
        nueva_coord = []
        for i in range(len(self.coord)):
            nueva_coord.append(self.coord[i] + otro.coord[i])
        return Vector(nueva_coord)

    def __mul__(self, num):
        nueva_coord = []
        for i in range(len(self.coord)):
            nueva_coord.append(self.coord[i] * num)
        return Vector(nueva_coord)


class Caja:
    def __init__(self, diccionario):
        for clave in diccionario:
            if clave not in [5, 10, 20, 50, 100, 200, 500, 1000]:
                raise ValueError(f"el billete {clave} no esta permitida")
        self.reg = diccionario

    def __str__(self):
        total = 0
        for clave, valor in self.reg.items():
            cant = clave * valor
            total += cant
        return f"Caja {self.reg} total: {total} pesos"

    def __add__(self, otro):
        if not isinstance(otro, dict):
            raise TypeError(f"{otro}no es un diccionario")
        ingreso = Caja(otro)
        for clave, valor in ingreso.reg.items():
            self.reg[clave] = self.reg.get(clave, 0) + valor

    def quitar(self, otro):
        if not isinstance(otro, dict):
            raise TypeError(f"{otro}no es un diccionario")
        ingreso = Caja(otro)
        for clave, valor in ingreso.reg.items():
            if clave in self.reg and self.reg[clave] > valor:
                nuevo_valor = self.reg[clave] - valor
                if nuevo_valor == 0:
                    self.reg.pop(clave)
                else:
                    self.reg[clave] = nuevo_valor
            else:
                raise ValueError(f"no hay suficientes billetes de denominacion {clave}")


class ListaEnlazada:
    def __init__(self, lista):
        if not isinstance(lista, list):
            raise TypeError("El elemento ingresado no es una lista")
        self.lista = lista

    def __str__(self):
        imprimir = ""
        for i in range(len(self.lista)):
            imprimir += str(self.lista[i]) + " "
        return imprimir

    def remover_todos(self, n):
        posiciones = []
        for i in range(len(self.lista)):
            if self.lista[i] == n:
                posiciones.append(i)
        for j in reversed(posiciones):
            self.lista.pop(j)

    def duplicar(self, n):
        for i in range(len(self.lista)):
            if self.lista[i] == n:
                self.lista[i] = self.lista[i] * 2

    def filter(self, f):
        nueva = []
        for i in self.lista:
            if f(i):
                nueva.append(i)

    def reversa(self):
        return self.lista[::-1]
