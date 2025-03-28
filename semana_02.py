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

#Ejercicio 3a

Equipos = {
    "River": ["Gallardo", "Libertadores"],
    "Boca": ["Gago", "Nada", "Tristeza"],
}

def contar_definiciones(d):
    #Creo un diccionario nuevo vacio para almacenar las respuestas
    nuevo_diccionario = {}

    for clave in d: #itero sobre cada clave en el diccionario original
        cantidad_definiciones = len(d[clave]) #calcula la cantidad de claves en el diccionario

        nuevo_diccionario[clave] = cantidad_definiciones #agrega la clave y el valor al nuevo diccionario

    return nuevo_diccionario

print(contar_definiciones(Equipos))

#Ejercicio 3b

def cantidad_de_claves_letra(d, l):
    contador = 0
    
    for clave in d:
        if clave.lower().startswith(l.lower()):
            # .lower() convierte todo el string en minusculas
            # .startswith() verifica si el string empieza con la letra indicada
            contador +=1
    return contador

print(cantidad_de_claves_letra(Equipos, "l"))

#Ejercicio 4

fosforos_1 = [0, -1, 1, 0, 0, -1, 0, 1, 0, 0]
fosforos_2 = [0, 0, 0, 0, 0, 1, 0, 0, -1, 0]


def propagar(fosforos):
    for i in range(len(fosforos)):
        if fosforos[i] == 1: #solo se propaga si i es 1
            j = i - 1 # Propagacion hacia la izquierda
            while j >= 0 and fosforos[j] == 0: #Mientras que haya fosforos nuevos hacia la izquierda
                fosforos[j] = 1 #se propaga el fuego
                j -= 1 #se mueve a la izquierda, necesario porque implicitamnte el for avanza hacia la derecha

            j = i + 1 # Propagacion hacia la derecha
            while j < len(fosforos) and fosforos[j] == 0: #Mientras que haya fosforos nuevos hacia la derecha
                fosforos[j] = 1 #se propaga el fuego
                #j += 1 #no es necesario porque, implicitamnte el for avanza hacia la derecha
    return fosforos

                

print(propagar(fosforos_1))
print(propagar(fosforos_2))




          






        
