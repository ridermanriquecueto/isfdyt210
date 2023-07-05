class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def obtener_nodo_anterior(self, nodo):
        return nodo.anterior.valor if nodo.anterior else None

    def obtener_nodo_siguiente(self, nodo):
        return nodo.siguiente.valor if nodo.siguiente else None
      
    def mostrar_lista(self,indice):
        for i in range(indice):
            valor = int(input("Ingresa el valor del elemento {}: ".format(i+1)))
        lista.agregar_elemento(valor)





# Crea una lista enlazada ingresando datos desde teclado
# lista = ListaEnlazada()


# while True:
#     valor = input("Ingrese un valor (o 'fin' para terminar): ")
#     if valor == "fin":
#         break
#     lista.agregar_elemento(valor)


# # Accede al nodo anterior y posterior de un nodo específico
# indice = int(input("Ingrese el índice del nodo a consultar: "))
# nodo_actual = lista.primero
# for _ in range(indice):
#     nodo_actual = nodo_actual.siguiente

# print("Valor actual:", nodo_actual.valor)
# print("Nodo anterior:", lista.obtener_nodo_anterior(nodo_actual))
# print("Nodo siguiente:", lista.obtener_nodo_siguiente(nodo_actual))
