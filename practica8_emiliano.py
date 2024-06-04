#ejercicio 22
from queue import LifoQueue as Pila
def visitar_sitio(historiales:dict[str,Pila[str]],usuario:str,sitio:str):
    if usuario not in historiales.keys():
        historiales[usuario]=Pila()
    historiales[usuario].put(sitio)
    return historiales[usuario].queue
def navegar_atras(historiales_nuevo:dict[str,Pila[str]],usuario:str):
    historiales_nuevo[usuario].get()
    return historiales_nuevo[usuario].queue
mi_pila=Pila()
mi_pila.put('facebook')
mi_pila.put('whatsapp')

print(visitar_sitio({'usuario1':mi_pila},'usuario1','instagram'))
print(navegar_atras({'usuario1':mi_pila},'usuario1'))
