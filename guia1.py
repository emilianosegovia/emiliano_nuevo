import csv
# Nombre del archivo CSV
nombre_archivo = 'arbolado-en-espacios-verdes.csv'

def leer_parque(nombre_archivo,parque):
    lista=[]
    with open(nombre_archivo,mode='rt',encoding='utf-8') as archivo:
        lector_csv=csv.reader(archivo,delimiter=',')
        primer_linea=next(lector_csv)

        for linea in lector_csv:
            if len(linea) > 10:
                if linea[10]==parque:
                    diccionario=dict()
                    for i in range(len(primer_linea)):
                        diccionario[primer_linea[i]]=linea[i]
                    lista.append(diccionario)
    return lista
#ejercicio 2
def especies(lista_de_arboles):
    lista=[]
    for arbol in lista_de_arboles:
        clave_valor=arbol.items()
        for (i,n) in clave_valor:
            if i == "nombre_com" and (n not in lista):
                lista.append(n)
    return lista
            
#ejercicio 3
def contar_ejemplares(lista_de_arboles):
    diccionario=dict()
    for arbol in lista_de_arboles:
        clave_valor=arbol.items()
        for (i,n) in clave_valor:
            if i=="nombre_com"and(n not in diccionario.keys()):
                diccionario[n]=1
            elif i=="nombre_com"and (n in diccionario.keys()):
                diccionario[n]+=1
    return diccionario

#ejercicio 4
def obtener_alturas(lista_de_arboles,especies):
    lista=[]
    for arbol in lista_de_arboles:
        clave_valor=arbol.items()
        for (i,n) in clave_valor:
            if i=="nombre_com" and (n==especies):
                lista.append(arbol['altura_tot'])
    return lista
def altura_promedio(x):
    numero=0
    for i in x:
        numero+=int(i)
    return numero/len(x)
def maximo(x):
    maximo_p=0
    for i in x:
        if int(i)>=maximo_p:
            maximo_p=int(i)
    return maximo_p
        
#ejercicio 5
def obtener_inclinaciones(lista_de_arboles,especies):
    lista=[]
    for arbol in lista_de_arboles:
        clave_valor=arbol.items()
        for (i,n) in clave_valor:
            if i=="nombre_com" and (n==especies):
                lista.append(arbol['inclinacio'])
    return lista
#ejercicio 6
def especimen_mas_inclinado(lista_de_arboles):
    maximo=0
    hola=""
    for arbol in lista_de_arboles:
        if int(arbol['inclinacio']) >= maximo:
            maximo=int(arbol['inclinacio'])
            hola=arbol['nombre_com']
    return((maximo,hola))
def promedio_inclinacion(lista_arboles, especies):
    suma_inclinacion = {}
    cuenta_arboles = {}
    
    # Recorremos la lista de árboles
    for arbol in lista_arboles:
        nombre_com = arbol['nombre_com']
        
        # Verificamos si la especie del árbol está en la lista de especies
        if nombre_com in especies:
            inclinacion = arbol['inclinacio']
            
            # Sumamos las inclinaciones y contamos los árboles para cada especie
            if nombre_com not in suma_inclinacion:
                suma_inclinacion[nombre_com] = inclinacion
                cuenta_arboles[nombre_com] = 1
            else:
                suma_inclinacion[nombre_com] += inclinacion
                cuenta_arboles[nombre_com] += 1
    
    # Calculamos el promedio de inclinación para cada especie
    promedio = {especie: suma_inclinacion[especie] / cuenta_arboles[especie] for especie in suma_inclinacion}
    
    return [promedio]

#ejercicio 7
def especie_promedio_mas_inclinada(lista_arboles):
    nuevas_especies=especies(lista_arboles)
    promedio_total=promedio_inclinacion(lista_arboles,nuevas_especies)
    maximo=(-1)
    hola=""
    for arbol in promedio_total:
        clave_valor=arbol.items()
        for (i,n) in clave_valor:
            if n>=maximo:
                hola=i
                maximo=n
    return (hola,maximo)
import pandas as pd
arboles_veredas='arbolado-publico-lineal-2017-2018.csv'
df_veredas=pd.read_csv(arboles_veredas)
data_arboles_veredas=df_veredas[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho','altura_arbol']]
print(data_arboles_veredas)
#ejercicio 8
df_nuevo=arboles_veredas.copy()
df_nuevo2=nombre_archivo.copy()

#lista_arboles_general_paz = leer_parque(nombre_archivo, 'CENTENARIO')
#especies_general_paz = especimen_mas_inclinado(lista_arboles_general_paz)
#print(especies_general_paz)