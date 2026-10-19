# Strings

my_string = "My String"
my_other_string = 'My String'

print(len(my_string))
print(len(my_other_string))


print(my_string + " " + my_other_string)


my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String\n\tcon tabulación"  #Ves que el salto de línea y la tabulación funcionan , pero no se ve el tabulado en la primera línea , para eso usamos el caracter de escape \ antes del caracter de tabulación
print(my_scape_string)                                     #Si pones doble barra , se cancela la tabulacion y el salto de línea , es decir , se imprime tal cual lo escribiste



# Formateo de Strings

name , surname , age = "Carlos" , "Núñez" , 14


print("Mi nombre es {} {} y tengo {} años". format(name , surname , age) ) #Muy típico cuando internacionalizamos texto

#Se puede de ambas formas ,con el .format() o con el %s , aunque el  .format() es más moderno y recomendable 

print("Mi nombre es %s %s y tengo %d años" %(name , surname , age) )

print("Mi nombre es " + name + " " + surname + " " + "y tengo " + str(age) + "años")
#Esta es la forma más antigua y menos recomendable de formatear strings , se llama concatenación de strings

print(f"Mi nombre es {name} {surname} y tengo {age} años") 
#Esta es la forma más moderna y recomendable de formatear strings , se llama f-strings


# Desempaquetado de caracteres

language = "python"
a , b, c , d, e, f = language
print(f) #Para leerlo al reves
print(e)
print(d)
print(c)
print(b)
print(a)

# División

language_slice = language[1:3] #El primer número es el índice de inicio , el segundo número es el índice de fin (no se incluye el índice de fin)
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)                #python

language_slice = language[-3:-1]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#Reverse language

reversed_language = language[:: -1]#El primer número es el índice de inicio , el segundo número es el índice de fin (no se incluye el índice de fin) , el tercer número es el paso (si es negativo , se lee al reves)
print(reversed_language)


# Funciones

print(language.capitalize())#Se pone la primera letra en mayúscula
print(language.upper())#Se ponen todas las letras en mayúscula
print(language.count("t"))#Cuenta la cantidad que hay de la letra que pongas entre comillas
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.startswith("to"))
print(language.startswith("Py"))
print("Py" == "py")#No es lo mismo
print(language.index("t"))


