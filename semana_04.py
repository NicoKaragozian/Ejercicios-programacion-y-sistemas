#%%
import csv

arbolado_csv = 'arbolado-en-espacios-verdes.csv'

def parques_disponibles(nombre_archivo):
    parques = set()
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            parques.add(fila["espacio_ve"])
    return parques


#Ejercico 1
def arboles_parque (nombre_archivo, nombre_parque):
    diccionario_parque = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["espacio_ve"] == nombre_parque:
                id_arbol = fila["id_arbol"]
                diccionario_parque[id_arbol] = fila
    return diccionario_parque

#prueba = arboles_parque(arbolado_csv, "INDOAMERICANO")
#for i, (id_arbol, datos) in enumerate(prueba.items()):
#    print(f"ID árbol: {id_arbol}")
 #   print("Datos:", datos)
  #  print("-" * 40)
    
   # if i == 2:  # Mostramos solo los primeros 3
    #    break

#Ejercicio 2
def arbol_mas_popular(nombre_parque):
    cantidad_arboles = {}
    arboles = arboles_parque(arbolado_csv, nombre_parque)
    for arbol in arboles.values():
        if arbol["nombre_com"] in cantidad_arboles:
            cantidad_arboles[arbol["nombre_com"]] += 1
        else:
            cantidad_arboles[arbol["nombre_com"]] = 1
    
    #return cantidad_arboles
    
    mas_popular = max(cantidad_arboles, key=cantidad_arboles.get)
    return mas_popular

#prueba = arbol_mas_popular("INDOAMERICANO")
#print(f"El árbol más popular en el parque es: {prueba}")

#Ejercicio 3
def n_mas_altos(nombre_parque, n):
    
    arboles_mas_altos = {}

    arboles = arboles_parque(arbolado_csv, nombre_parque)

    for arbol in arboles.values():
        nombre = arbol["nombre_com"]
        altura = float(arbol["altura_tot"])
        if nombre not in arboles_mas_altos:
            arboles_mas_altos[nombre] = altura
        else:
            if altura > arboles_mas_altos[nombre]:
                arboles_mas_altos[nombre] = altura
    
    arboles_altos = list(arboles_mas_altos.items())

    arboles_ordenados = sorted(arboles_altos, key=lambda x: x[1], reverse=True)

    return arboles_ordenados[:n]

#prueba = n_mas_altos("INDOAMERICANO", 5)
#print (prueba)

#Ejercicio 4
def altura_promedio(nombre_parque, especie):
    arboles = arboles_parque(arbolado_csv, nombre_parque)
    suma_altura = 0
    cantidad_arboles = 0
    for arbol in arboles.values():
        if arbol["nombre_com"] == especie:
            suma_altura += float(arbol["altura_tot"])
            cantidad_arboles += 1
    if cantidad_arboles == 0:
        return "No hay árboles de esta especie en el parque."
    return suma_altura / cantidad_arboles

#prueba = altura_promedio("INDOAMERICANO", "Eucalipto")
#print (prueba)

#Ejercicio 5
def parques_mas_arboles(n):
    cantidad_por_parque = {}

    with open(arbolado_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            parque = fila["espacio_ve"]
            if parque in cantidad_por_parque:
                cantidad_por_parque[parque] += 1
            else:
                cantidad_por_parque[parque] = 1

    parques_ordenados = sorted(cantidad_por_parque.items(), key=lambda x: x[1], reverse=True)
    return parques_ordenados[:n]

#prueba = parques_mas_arboles(5)
#print(prueba)

def alturas_por_parque():
    alturas = {}
    cantidades = {}
    with open(arbolado_csv, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            parque = fila["espacio_ve"]
            altura = float(fila["altura_tot"])

            if parque in alturas:
                alturas[parque] += altura
                cantidades[parque] += 1
            else:
                alturas[parque] = altura
                cantidades[parque] = 1

    promedios = []
    for parque in alturas:
        promedio = alturas[parque] / cantidades[parque]
        promedios.append((parque, promedio))

    return promedios


def parques_mas_altos_promedio(n):
    promedios = alturas_por_parque()
    return sorted(promedios, key=lambda x: x[1], reverse=True)[:n]


#prueba = parques_mas_altos_promedio(5)
#print(prueba)

def especies_por_parque():
    especies = {}

    with open(arbolado_csv, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            parque = fila["espacio_ve"]
            especie = fila["nombre_com"]

            if parque not in especies:
                especies[parque] = set()

            especies[parque].add(especie)

    # Convertimos a lista de tuplas (parque, cantidad de especies)
    variedad = [(parque, len(especies[parque])) for parque in especies]
    return variedad


def parques_mas_diversos(n):
    variedad = especies_por_parque()
    return sorted(variedad, key=lambda x: x[1], reverse=True)[:n]

#prueba = parques_mas_diversos(5)
#print(prueba)

def especie_mas_comun():
    conteo = {}
    with open(arbolado_csv, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            especie = fila["nombre_com"]
            conteo[especie] = conteo.get(especie, 0) + 1
    return max(conteo.items(), key=lambda x: x[1])

#prueba = especie_mas_comun()
#print(f"La especie más común es: {prueba[0]} con {prueba[1]} ejemplares.")

def razon_exoticas_autoctonas():
    exoticas = 0
    autoctonas = 0
    with open(arbolado_csv, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            origen = fila["origen"].strip().lower()
            if origen == "exótico":
                exoticas += 1
            elif origen == "nativo/autóctono":
                autoctonas += 1
    if autoctonas == 0:
        return float('inf')
    return exoticas / autoctonas

#prueba = razon_exoticas_autoctonas()
#print(f"La razón de árboles exóticos a autóctonos es: {prueba:.2f}")

if __name__ == "__main__":

    print("\n--- Parques con mayor cantidad de árboles ---")
    for parque, cantidad in parques_mas_arboles(5):
        print(f"{parque}: {cantidad} árboles")

    print("\n--- Parques con árboles más altos en promedio ---")
    for parque, promedio in parques_mas_altos_promedio(5):
        print(f"{parque}: altura promedio {promedio:.2f} m")

    print("\n--- Parques con más variedad de especies ---")
    for parque, cantidad in parques_mas_diversos(5):
        print(f"{parque}: {cantidad} especies distintas")

    print("\n--- Especie más frecuente en la ciudad ---")
    especie, cantidad = especie_mas_comun()
    print(f"{especie}: {cantidad} ejemplares")

    print("\n--- Razón entre especies exóticas y autóctonas ---")
    razon = razon_exoticas_autoctonas()
    print(f"Razón exóticas/autóctonas: {razon:.2f}")

# %%
