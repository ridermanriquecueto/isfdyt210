class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.primer_nodo = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            nodo_actual = self.primer_nodo
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def recorrer_lista(self):
        nodo_actual = self.primer_nodo
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

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
