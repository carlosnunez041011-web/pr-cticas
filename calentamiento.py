



'''class Gastos:
    def __init__(self):
        self.concepto = input("Introduce el concepto: ").capitalize()
        while True:
            try:
                self.importe = float(input("Introduce el importe: "))
                break
                
            except ValueError:
                print("ValueError , you must introduce a number")
                
        
        

    def final(self):
        return(f"{self.concepto}:{self.importe}€")


gasto_1 = Gastos()
print(gasto_1.final())'''



productos = {
    "pan":1.00,
    "hamburguesa":9.00,
    "leche":5.00,
    "pimiento":3.00
}


'''def pedir_productos(dict):
    lista_compra = {}
    while True:
        peticion = input("Introduce el producto(introduzca fin si no quiere añadir más productos): ").lower()
        if peticion == "fin":
            break
        if peticion in dict:
            precio =dict[peticion]
            lista_compra[peticion] = precio
        else:
            print("El producto no está disponible")
            
        
        return lista_compra

        



def lista_ordenada(dict): 
    print("---Lista de compra---\n")
    for producto,precio in dict.items():
        print(f"{producto}:{precio}€")
   


def suma_total(dict):
    total_sum = 0
    for num in dict.values():
        total_sum+= num
        
    return (f"\nTotal a pagar: {total_sum}€")

recibo =pedir_productos(productos)
lista_ordenada(recibo)
print(suma_total(recibo))'''








#peticion = "pan"
#precio = productos[peticion] te devuelve el valor de la clave "peticion" que es pan 
#print(precio) 



'''def añadir_tareas(tareas,texto):
    tareas.append({"tarea":texto,"completada":False})

def completar_tarea(tareas,numero):
    if 1 <= numero <= len(tareas):
        tareas[numero - 1]["completada"] = True

def listar_tareas(tareas):
    numero = 1
    for tarea in tareas:
        if tarea["completada"] == True:
            estado = "completada"
        else:
            estado = "pendiente"
        print(f"{numero}. {tarea["tarea"]}-{estado}")
        numero += 1
def tareas_pendientes(tareas):
    contador = 0
    for tarea in tareas:
        if tarea["completada"] == False:
            contador += 1
    return (f"Tareas pendientes: {contador}")


tareas = []

while True:
    añadir_tarea = input("Añade una tarea(pon salir para finalizar): ").lower()
    if añadir_tarea == "salir":
        break
    añadir_tareas(tareas,añadir_tarea)
    

    
completar_tarea(tareas,2)
completar_tarea(tareas,3)
listar_tareas(tareas)
tareas_pendientes(tareas)

'''
import random
from random import randint
import json
from pathlib import Path

RECORD_HISTORIAL = Path(__file__).with_name("record_historial.json")

## COSAS QUE TENGO:
 # Historial para el record
## COSAS QUE NECESITO:
 # Jugador 1 jugador 2 , historial de todas las partidas a parte en otro archivo aunque no sean record, 
 # añadir tmb el numero maximo de intentos permitido por nivel al historial




while True: 
    num_1 = 0
    num_2 = 0
    num_intentos = 0
    dificultad = input("Introduce nivel de dificultad(fácil/media/difícil): ").lower()
    if dificultad == "fácil"or dificultad == "facil":
        num_1 = 1
        num_2= 10
        num_intentos = 5
    elif dificultad == "media":
        num_1 = 1
        num_2 = 100
        num_intentos = 10
    elif dificultad == "dificil"or dificultad == "difícil":
        num_1 = 1 
        num_2 = 1000
        num_intentos = 15
    else:
        print("Dificultad no válida. Inténtelo otra vez")
        continue

    def numero_aleatorio(num_1,num_2):
        numero = random.randint(num_1,num_2)
        return numero
    
    def adivinar_numero(numero):
        contador = 0
        while True:
            try:
                adivinar = int(input("Adivina un número: "))
            except ValueError:
                print("Dato no válido, inténtelo otra vez")
                continue
            if adivinar == numero :
                print(f"Has adivinado, el número era {numero}")
                print(f"Número de intentos: {contador}")
                break
            else:
                contador +=1
                if adivinar < numero:
                    print("Incorrecto, el número es mayor")
                elif adivinar > numero:                     ## EN EL ELIF SOLO SE EJECUTA LA PRIMERA CONDICIÓN VERDADERA
                    print("Incorrecto, el número es menor")
                if contador < num_intentos:
                    print(f"Te quedan {num_intentos-contador} intentos")
                elif contador >= num_intentos:
                    print("Se te han acabado los intentos")
                    print(f"El número era {numero}")
                    break
        return contador , True
    intentos, ganada = adivinar_numero(numero_aleatorio(num_1,num_2))
    def cargar_historial(ruta):
        try:
            with open(ruta,"r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []

    def guardar_partida(ruta,partida):
        historial = cargar_historial(ruta)
        historial.append(partida)
        with open(ruta,"w", encoding="utf-8") as archivo:
            json.dump(historial, archivo, ensure_ascii=False, indent = 4)
    partida = {
        "dificultad":dificultad,
        "Número de intentos":intentos
        }
    if ganada:
        partida["Partida"] = "Ganada"
    else:
        partida["Partida"] = "Perdida"
    

    guardar_partida(RECORD_HISTORIAL,partida)

    volver_jugar = input("¿Quieres volver a jugar?: ").lower()

    if volver_jugar == "no":
        print('El juego ha finalizado')
        break
    elif volver_jugar=="si"or"sí":
        continue




        
  



    


    

        





        









    
    




    

    




      
        


    
    





        

    