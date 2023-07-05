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

    def eliminar_elemento(self, dato):
        if self.primer_nodo is None:
            return
        
        if self.primer_nodo.dato == dato:
            self.primer_nodo = self.primer_nodo.siguiente
            return
        
        nodo_actual = self.primer_nodo
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.dato == dato:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

    def recorrer_lista(self):
        nodo_actual = self.primer_nodo
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
