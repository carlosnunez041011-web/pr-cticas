##Modulos##
## Un modulo (import) hace que puedas utilizar en un programa , funciones de otros ,etc
import my_module
from my_module import printValue,sum ## caundo importas una funcion de un modulo no te hace falta escribir el my_module solo escribes la función
#from 010_funcitons import sum_two_values   ## 010_funcitons NO es valido para importar modulos . hay que cambiarle el nombre
## from 010_funcitons import sum_two_values se reifere a dentro del modulo , coger una función concreta
my_module.sum(5,5,5)
my_module.printValue("Hola Carlos")

printValue("Hola Carlos")
sum(5,5,5)

import math

print(math.pi)
print(int(math.pow(2,3)))

from math import pi as PI_VALUE ## Le puedes poner un alias a la funcion o module

print(PI_VALUE)


