def encontrar_maximo_minimo():
    n = int(input("Ingresa el número de elementos: "))
    
    if n == 0:
        print("No hay elementos para encontrar máximo y mínimo.")
        return
    
    numeros = []
    
    for i in range(n):
        numero = float(input("Ingresa el número {}: ".format(i + 1)))
        numeros.append(numero)
    
    maximo = max(numeros)
    minimo = min(numeros)
    
    print("El máximo es:", maximo)
    print("El mínimo es:", minimo)

# Llamada a la función para encontrar máximo y mínimo
encontrar_maximo_minimo()
