#Ejercicio figuritas

import random 
import numpy as np

#Datos del problema
#Álbum con 860 figuritas.
#Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#Cada paquete trae cinco figuritas.

figus_total = 860
#Creo la funcion que crea el album vacio
def crear_album(figus_total):
    """Crea un album con 860 figuritas, todas en cero."""
    album = [0] * figus_total #Crea una lista de 860 elementos, todos en cero.
    return album

#album = crear_album(figus_total)
#print(album)

#Devuelve false solo si todo el album es distinto a 0
def album_incompleto(A):
    for i in range(len(A)):
        if A[i] == 0:
            return True
    return False

#print(album_incompleto(album))

#Funcion que devuelve un numero random entre 0 y 859
def comprar_figu(figus_total):
    figu = random.randint(0, figus_total - 1) #Genera un numero aleatorio entre 0 y 859
    return figu

#prueba = comprar_figu(figus_total)
#print(prueba)

#Ejercicio 4
def cuantas_figus(figus_total):
    album = crear_album(figus_total) #Crea el album vacio
    figuritas_compradas = 0 #Contador de paquetes comprados

    while album_incompleto(album): #Mientras el album no este completo
        figu = comprar_figu(figus_total) #Compra una figurita
        figuritas_compradas += 1 #Aumenta el contador de figuritas compradas
        album[figu] += 1

    return figuritas_compradas #Devuelve el contador de figuritas compradas
    
#prueba = cuantas_figus(figus_total)
#print(prueba)


