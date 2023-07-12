class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        encontrado = False
        while actual and not encontrado:
            if actual.dato == dato:
                encontrado = True
            else:
                anterior = actual
                actual = actual.siguiente
        if actual is None:
            return
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()


lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

print("Lista original:")
lista.imprimir()

lista.eliminar(3)

print("Lista después de eliminar el nodo con dato 3:")
lista.imprimir()