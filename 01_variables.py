#Variables
# Este es el dia 2/30 aprendiendo python , para mi yo del futuro , recuerda mirar y hacer los ejercicios de practica del dia 2
my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema 
print(len(my_string_variable))   # len() es una función que nos permite conocer la longitud de un string

# Variables en una sola línea , se puede hacer pero no es muy recomendable , lo mejor es declarar cada variable en una línea diferente
name, surname, alias, age = "Carlos", "Núñez", "Cuco", 14
print("Me llamo:", name, surname, ", tengo:", age, "años", "y mi alias es:", alias)

# Inputs
#name = input("¿Como te llamas? ")
#age = input("¿Cuantos años tienes? ")

#print(name)
#print(age)

# Cambiamos su type
name = 14
age = "Carlos"
print(name)
print(age)

#¿Forzamos el tipo? , aunque le pongamos un tipo de dato a una variable , si le asignamos un valor de otro tipo de dato , el tipo de dato cambia

adress: str = "Mi direccion"
adress = 32
print(adress)
print(type(adress))

first_name = "Carlos"
last_name = "Núñez"
full_name = "Carlos Núñez"
country = "España"
city = "Madrid"
age = 14
year = 2026
is_married, is_light_on = False, True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

print(len(last_name) - (len(first_name)))

num_1 = 5
num_2 = 4

variable_total = num_1 + num_2
variable_diff = num_2 - num_1
variable_product = num_1 * num_2
variable_division = num_2 / num_1
variable_remainder = num_1 % num_2
variable_exp = num_1 ** num_2
variable_floor_division = num_1 // num_2
radius_of_circle = 30
import math
pi = math.pi
area_of_circle = pi * 30**2
resultado_area = round(area_of_circle)
circum_of_circle = 2 * pi * radius_of_circle
resultado_circum = round(circum_of_circle)


print(variable_total)
print(variable_diff)
print(variable_product)
print(variable_division)
print(variable_remainder)
print(variable_exp)
print(variable_floor_division)
print(f"{resultado_area} m")
print(f"{resultado_circum} m")

first_name = input("Nombre: ")
last_name = input("Apellidos: ")
age = input("Edad: ")
country = input("País: ")


import math

pi = math.pi

radius = float(input("El radio del círculo es: "))
unit = input("Introduce la unidad abreviada: ").strip().lower()

area = pi * radius ** 2
area = round(area, 2)

print(f"El área del círculo es: {area} {unit}²")