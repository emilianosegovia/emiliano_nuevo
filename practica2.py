import csv
# Nombre del archivo CSV
nombre_archivo = 'cronograma_sugerido.csv'

def materias_cuatrimestre(nombre_archivo,n):
    lista=[]
    diccionario=dict()
    with open(nombre_archivo,mode='rt') as archivo:
        lector_csv=csv.reader(archivo,delimiter=';')
        next(lector_csv)
        for linea in lector_csv:
            for i in range(len(linea)):
                if int(linea[0])==(n):
                    diccionario[lector_csv[0][i]]=linea[i]
                lista.append(diccionario)
    return lista
print(materias_cuatrimestre(nombre_archivo, 3))