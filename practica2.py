import csv
# Nombre del archivo CSV
nombre_archivo = 'cronograma_sugerido.csv'

def materias_cuatrimestre(nombre_archivo,n):
    lista=[]
    with open(nombre_archivo,mode='rt') as archivo:
        lector_csv=csv.reader(archivo,delimiter=';')
        primer_linea=next(lector_csv)
        for linea in lector_csv:
            if int(linea[0])==(n):
                diccionario=dict()
                for i in range(len(primer_linea)):
                    diccionario[primer_linea[i]]=linea[i]
                lista.append(diccionario)
    return lista
print(materias_cuatrimestre(nombre_archivo, 3))