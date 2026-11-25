import json
from pathlib import Path

RUTA_JUGADOR = Path(__file__).with_name("jugador.json")

while True:
    def guardar_json(ruta,datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4,ensure_ascii=False)


    def cargar_ruta_json(ruta): 
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    try:
        jugador = cargar_ruta_json(RUTA_JUGADOR)
    except (FileNotFoundError, json.JSONDecodeError):
        jugador = []
    nombre = input("Nombre del jugador: ").capitalize()
    puntos = int(input("Puntos del jugador: "))
    nuevo_jugador = {"nombre":nombre,
                    "puntos":puntos,
                    }
    for existente in jugador:
        if existente["nombre"] == nuevo_jugador:
            existente["puntos"] = nuevo_jugador["puntos"]
    else:   ### El else va fuera del for porque el else solo añade al jugador si la busqueda termina sin encontrarlo
        jugador.append(nuevo_jugador)
        guardar_json(RUTA_JUGADOR,jugador)
    pregunta_final= input("¿Quiere añadir otro jugador?: ").lower()
    if pregunta_final == "si" or pregunta_final== "sí":
        continue
    else:
        break
    

    

