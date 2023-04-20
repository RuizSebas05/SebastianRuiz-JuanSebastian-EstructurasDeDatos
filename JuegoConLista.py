import random


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None


class Matriz:
    def __init__(self, n):
        self.n = n
        self.matriz = [[None] * n for _ in range(n)]
        simbolos = [" ", " ", " ", " ", "+", "-", " "]

        for i in range(n):
            for j in range(n):
                self.matriz[i][j] = Nodo(random.choice(simbolos))

                if i > 0:
                    self.matriz[i][j].arriba = self.matriz[i - 1][j]
                if i < n - 1:
                    self.matriz[i][j].abajo = self.matriz[i + 1][j]
                if j > 0:
                    self.matriz[i][j].izquierda = self.matriz[i][j - 1]
                if j < n - 1:
                    self.matriz[i][j].derecha = self.matriz[i][j + 1]

        for i in range(n - 1):
            self.matriz[i][0].izquierda = None
            self.matriz[i][n - 1].derecha = None

        for j in range(n - 1):
            self.matriz[0][j].arriba = None
            self.matriz[n - 1][j].abajo = None

    def mostrar_matriz(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.matriz[i][j].valor, end=", ")
            print()


class Alien:
    def __init__(self, vida=50):
        self.vida = vida
        self.posicion = None

    def elegir_posicion_alien(self, matriz):
        while True:
            fila = int(input("Ingrese la fila donde desea ubicar al Alien: "))
            columna = int(input("Ingrese la columna donde desea ubicar al Alien: "))
            nodo = matriz.matriz[fila][columna]
            if nodo.valor == " ":
                self.posicion = (fila, columna)
                nodo.valor = "A"
                break
            else:
                print("Esa posición no está disponible. Por favor, elija otra.")

    def mostrar_vida(self):
        print(f"Vida del Alien: {self.vida}")

    def mover_alien(self, matriz):
        while True:
            direccion = input("Ingrese la dirección hacia donde desea mover al Alien (arriba, abajo, izquierda, "
                              "derecha): ")
            fila, columna = self.posicion
            if direccion == "arriba":
                if fila > 0:
                    nodo = matriz.matriz[fila - 1][columna]
                    if nodo.valor == " ":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        break
                    elif nodo.valor == "+":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        self.vida += 10
                        break
                    elif nodo.valor == "-":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        self.vida -= 10
                        break
            elif direccion == "abajo":
                if fila < matriz.n - 1:
                    nodo = matriz.matriz[fila + 1][columna]
                    if nodo.valor == " ":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila + 1, columna)
                        break
                    elif nodo.valor == "+":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila + 1, columna)
                        self.vida += 10
                        break
                    elif nodo.valor == "-":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        self.vida -= 10
                        break
            elif direccion == "izquierda":
                if columna > 0:
                    nodo = matriz.matriz[fila][columna - 1]
                    if nodo.valor == " ":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila, columna - 1)
                        break
                    elif nodo.valor == "+":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila, columna - 1)
                        self.vida += 10
                        break
                    elif nodo.valor == "-":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        self.vida -= 10
                        break
            elif direccion == "derecha":
                if columna < matriz.n - 1:
                    nodo = matriz.matriz[fila][columna + 1]
                    if nodo.valor == " ":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila, columna + 1)
                        break
                    elif nodo.valor == "+":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila, columna + 1)
                        self.vida += 10
                        break
                    elif nodo.valor == "-":
                        nodo.valor = "A"
                        matriz.matriz[fila][columna].valor = " "
                        self.posicion = (fila - 1, columna)
                        self.vida -= 10
                        break
            print("Movimiento inválido. Por favor, intente de nuevo.")

        matriz.mostrar_matriz()


class Depredador:
    def __init__(self, vida=50):
        self.vida = vida
        self.posicion = None

    def mover_depredador(self):
        pass

    def ubicar_en_matriz(self, matriz):
        n = matriz.n
        i = random.randint(0, matriz.n - 1)
        j = random.randint(0, matriz.n - 1)
        nodo = matriz.matriz[i][j]
        self.posicion = (i, j)
        nodo.valor = "D"

    def Mostrar_Vida(self):
        print(f"Vida del Depredador: {self.vida}")


def juego(n):
    matriz = Matriz(n)
    depredador = Depredador()
    depredador.ubicar_en_matriz(matriz)
    matriz.mostrar_matriz()
    depredador.Mostrar_Vida()
    alien = Alien()
    alien.elegir_posicion_alien(matriz)
    # imprimir matriz con el depredador y el alien ubicados
    matriz.mostrar_matriz()
    depredador.Mostrar_Vida()
    alien.mostrar_vida()

    while True:
        alien.mover_alien(matriz)
        depredador.mover_depredador()
        depredador.Mostrar_Vida()
        alien.mostrar_vida()


A = int(input("Ingrese el tamaño de la matriz: "))
juego(A)
