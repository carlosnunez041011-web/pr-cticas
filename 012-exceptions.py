###Exception Handling##

number_one = 5
number_two = 1
number_two = "1"
#try except
try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    #Se ejecuta si se produce una excepción
    print("Se ha producido error")

#try except else

try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido error")
else:#Opcional
    #Se ejecuta si no se produce una excepcion 
    print("La ejecución continua correctamente")
finally:#Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")

#Excepciones por tipo
try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError:
    print("Se ha producido ValueError")
except TypeError:
    #Se ejecuta si se produce un TypeError
    print("Se ha producido TypeError")

#Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)

