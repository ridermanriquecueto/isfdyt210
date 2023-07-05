class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Crear la lista enlazada e ingresar valores desde el teclado
lista = ListaEnlazada()
n = int(input("Ingresa el número de elementos de la lista: "))
for i in range(n):
    valor = int(input("Ingresa el valor del elemento {}: ".format(i+1)))
    lista.agregar_elemento(valor)

# Mostrar la lista enlazada
print("La lista enlazada es:")
lista.mostrar_lista()
