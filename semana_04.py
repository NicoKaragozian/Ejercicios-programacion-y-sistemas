#%%
import csv

arbolado_csv = 'arbolado-en-espacios-verdes.csv'

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




    
    
                

# %%
