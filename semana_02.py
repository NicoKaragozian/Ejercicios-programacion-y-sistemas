# Ejercicio 1

lista = [1, 2, 3, 4, 5]

def invertir_lista(lista):
    return lista[::-1]

print(invertir_lista(lista))

# Ejercicio 2
def collatz(nro):
    if not isinstance(nro, int):  # Verificar que el número sea entero
        raise ValueError("El número debe ser un entero.")
    if nro <= 0:  # Verificar que el número sea positivo
        raise ValueError("El número debe ser un entero positivo.")

    pasos = 0 #contador para registrar la cantidad de pasos

    while nro != 1: #la funcion va a iterar hasta que el nro sea 1
        if nro % 2 == 0: #si el numero es par (porque el resto de dividir por dos es 0)
            nro = nro / 2 #divide el numero por 2
        else: #si el numero es impar
            nro = nro * 3 + 1 #multiplica el numero por 3 y le suma 1

        pasos += 1 #incrementa el contador de pasos

    return pasos

print(collatz(117))


        
