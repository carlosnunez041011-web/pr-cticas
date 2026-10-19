from random import randint



'''def adivinar_numero():
    contraseña = input("Introduce un número de 4 dígitos: ")
    intento = ""
    contador = 0
    while intento != contraseña:
        numero = randint(0,9999)
        intento = str(numero).zfill(4)
        contador += 1
        if intento == contraseña:
            print(f"Contraseña adivinada:{contraseña}")
            print(f"Número de intentos: {contador}")
            break
        else:
            print(f"Probando: {numero}")

adivinar_numero()

def adivinar_numero():
    contraseña = input("Introduce una contraseña de 4 dígitos: ")
    contador = 0
    intento = ""
    for numero in range(0,9999):
        intento=str(numero).zfill(4)
        contador += 1   
        if intento != contraseña:
            print(f"Probando:{intento}")
        elif intento == contraseña:
            print(f"Contraseña adivinada:{contraseña}")
            print(f"Número de intentos: {contador}")
            break

adivinar_numero()

import random
import string

def random_user_id():
    id = []
    caracteres = string.ascii_lowercase + string.digits
    numero_caracteres = int(input("Introduce el numero de caracteres: "))
    id_generados = int(input("Introduce el numero de id que quieres generar: "))
    
    for i in range(id_generados):
        id.append("".join(random.choices(caracteres,k=numero_caracteres)))
    return "\n".join(id)

print(random_user_id())'''


def rgb_colores():
   r = randint(0,255)
   g = randint(0,255)
   b = randint(0,255)
   rgb = (r,g,b)
   return rgb

print(rgb_colores())
import string
import random
def colores_hexadecimales():
    
    caracteres = string.ascii_lowercase + string.digits
    id_hashtag = []
        
    id="".join(random.choices(caracteres,k=6))
    id_hashtag.append("#"+id)

    return "\n".join(id_hashtag)

print(colores_hexadecimales())


'''def rgb_colores_lista():
    cantidad_colores = int(input("Introduce el número de colores que quieres: "))
    rgb_list = []
    rgb = ()
    for i in range(cantidad_colores):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        rgb = (r,g,b)
        rgb_list.append(f"rgb{rgb}")
    return rgb_list
   

print(rgb_colores_lista())'''


def tipo_color(tipo,cantidad):
    lista_rgb = []
    lista_hexa = []
    if tipo == "rgb":
        for i in range(cantidad):
            lista_rgb.append(rgb_colores())
        return lista_rgb
    elif tipo == "hexa":
        for i in range(cantidad):
            lista_hexa.append(colores_hexadecimales())
        return lista_hexa
    


print(tipo_color("hexa",6))


        







