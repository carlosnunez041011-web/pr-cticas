# Operadores aritméticos

print(3 + 4) # Suma
print(3 - 4) # Resta
print(3 * 4) # Multiplicación
print(3 / 4) # División
print(3 % 4) # Módulo
print(3 ** 4) # Potencia
print(3 // 4) # División entera
print(3 ** 4 + 5 / 2 - 2) # Operaciones combinadas


print(" Hola " + " Python " + " ¿Que tal? ")# Concatenación de strings
print(" Hola " + str(5)) # Estamos forzando a un numero entero o 'int' a que se convierta en un string o 'str'
print(" Hola " * 5) # Repetición de strings
print(" Hola " * (2 ** 3)) # Repetición de strings
print("Hola" * (8 ** 2 + 2))# Repetición de strings

my_float = 2.5 * 2
print("Hola" * int(my_float))# Repetición de strings


# Operadores comparativos
print(3 > 4)    # Mayor que
print(3 < 4)    # Menor que
print(3 >= 4)   # Mayor o igual que
print(3 <= 4)   # Menor o igual que
print(3 == 4)   # Igual que
print(3 != 4)   # Diferente de


# Ordenacion alfabetica 
print("Hola" > "Python") 
print("Hola" < "Python") 
print("Hola" >= "Zola") 
print("Hola" <= "Python")
print("Hola" == "Python") 
print("Hola" != "Python") 

#Ordenacion por numero de caracteres
print(len("Hola") > len("Python"))

#Operadores lógicos

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 and "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))
print(not(("Hola" > "Python" and 4 == 4) or 3 < 4))


age = 14
print(age)

height = 1.70
print(height)

complex_number = 4 + 3j
print(complex_number)


base_del_triangulo = float(input("Base del triángulo: "))
altura_del_triangulo = float(input("Altura del triángulo: "))
unit = input("Introduce la unidad abreviada: ")
area_del_triangulo = (base_del_triangulo * altura_del_triangulo) /2
resultado = area_del_triangulo
print(f"El area del tirángulo es {resultado} {unit}²")


lado_a = input("Introduce la longitud del primer lado del tirángulo: ")
lado_b = input("Introduce la longitud del segundo lado del tirángulo: ")
lado_c = input("Introduce la longitud del tercer lado del tirángulo: ")
unit = input("Introduce la unidad abreviada: ")

perímetro = lado_a + lado_b + lado_c
print(f"El perimetro es de {perímetro} {unit}")



# y = m * x + b (2,2) (6,10) y = 2x - 2
pendiente_1 = 2
corte_y = (0, -2)
corte_x = (1, 0)

print(f"Pendiente: {pendiente_1}")
print(f"Corte y: {corte_y}")
print(f"Corte x: {corte_x}")


x_1 = 2
y_1 = 2
x_2 = 6
y_2 = 10

pendiente_2 = (y_2 - y_1) / (x_2 - x_1)
distancia_euclidean = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** 0.5

print(f"La pendiente es: {pendiente_2}")
print(f"La distancia euclidean es: {distancia_euclidean}")


print(pendiente_1 == pendiente_2)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = float(input("Introduce el valor de x: "))

y = x ** 2 + 6 * x + 9

print(f"El valor de y es: {y}")


numero = int(input("Introduce un número entero: "))


if numero % 2 == 0 :
    print(f"El numero {numero} es par")
else : 
    print(f"El numero {numero} es impar")


