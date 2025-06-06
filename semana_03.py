#%%
import random 

#Datos del problema
#Álbum con 860 figuritas.
#Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
#Cada paquete trae cinco figuritas.
#Creo la funcion que crea el album vacio

def crear_album(figus_total):    
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
#Funcion que devuelve la cantidad de figuritas compradas para completar el album
def cuantas_figus(figus_total):
    album = crear_album(figus_total) #Crea el album vacio
    figuritas_compradas = 0 #Contador de paquetes comprados

    while album_incompleto(album): #Mientras el album no este completo
        figu = comprar_figu(figus_total) #Compra una figurita
        figuritas_compradas += 1 #Aumenta el contador de figuritas compradas
        album[figu] += 1

    return figuritas_compradas #Devuelve el contador de figuritas compradas

#Ejercicio 6
#Funcion que devuelve la cantidad de figuritas compradas para completar el album, dada n_repeticiones
def experimento_figus(n_repeticiones, figus_total):
    resultado = [cuantas_figus(figus_total) for _ in range(n_repeticiones)] #Lista con los resultados de cada repeticion
    promedio = sum(resultado)/ n_repeticiones #Promedio de figuritas compradas
    return promedio #Devuelve el promedio de figuritas compradas

#Funcion que devuelve un paquete de tamaño figus_paquete, con figuritas aleatorias dentro del album figus_total
def comprar_paquete(figus_total, figus_paquete):
    paquete = [comprar_figu(figus_total) for _ in range(figus_paquete)] #Lista con las figuritas del paquete
    return paquete #Devuelve el paquete

#Ejercicio 9
#Funcion que devuelve la cantidad de paquetes comprados para completar el album
def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total) #Crea el album vacio
    paquetes_comprados = 0 #Contador de paquetes comprados

    while album_incompleto(album): #Mientras el album no este completo
        paquete = comprar_paquete(figus_total, figus_paquete) #Compra un paquete
        paquetes_comprados += 1 #Aumenta el contador de paquetes comprados

        for figu in paquete:
            album[figu] += 1
    return paquetes_comprados #Devuelve el contador de paquetes comprados
    
#prueba = cuantas_figus(figus_total)
#print(prueba)
    # %%

if __name__ == "__main__":

    # Ejercicio 5
    n_repeticiones = 1000 #Numero de repeticiones
    figus_total = 6
    cant_figus = [cuantas_figus(figus_total) for _ in range(n_repeticiones)] #Lista con los resultados de cada repeticion
    promedio_figus = sum(cant_figus)/ n_repeticiones #Promedio de figuritas compradas
    # print(f"Promedio de figuritas compradas para album de 6 figuritas: {promedio_figus}")

    #Ejercicio 6  
    n_repeticiones = 100 #Numero de repeticiones
    figus_total = 860 #Numero de figuritas
    cant_figus = experimento_figus (n_repeticiones, figus_total) #Ejecuta el experimento de figuritas
    # print(f"Promedio de figuritas compradas para album de 860 figuritas: {cant_figus}")

    #Ejercicio 10
    n_repeticiones = 1000
    figus_total = 860
    figus_paquete = 5
    cant_paquetes = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)] #Lista con los resultados de cada repeticion
    promedio_paquetes = sum(cant_paquetes)/ n_repeticiones #Promedio de paquetes comprados
    # print(f"Promedio de paquetes comprados para album de 860 figuritas: {promedio_paquetes}")