### Funciones
### Si no apredno en esta clase lo de 'in range' lo busco en ChatGPT
### TERMINAR EL EJERCICIO NIVEL 3 DE LOOPS




from unicodedata import name


def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_value, second_value): ## Una función es un bloque de código que se puede reutilizar y que realiza una tarea específica. Se define con la palabra clave 'def' seguida del nombre de la función y paréntesis que pueden contener parámetros. El código dentro de la función se ejecuta cuando se llama a la función.
    print(first_value + second_value)                      ## Dentro de una funcion , poner los type, no sirve de nada



sum_two_values(5, 7)
sum_two_values(34354, 782873)
sum_two_values(int("5"), int("7"))


def sum_two_values_with_return(first_value, second_value): 
    total = first_value + second_value 
    return total  ## La palabra clave 'return' se utiliza para devolver un valor desde una función. Cuando se llama a la función, el valor devuelto puede ser asignado a una variable o utilizado directamente en una expresión.


my_result = sum_two_values_with_return(10, 5) 
print(my_result)


def print_full_name(name, surname):
    print(f"{name} {surname}")

print_full_name(surname = "Núñez", name = "Carlos") ## Le he cambiado el orden a los parámetros y no pasa nada porque he puesto el nombre de los parámetros en la llamada a la función. Esto se llama 'keyword arguments' y es una forma de pasar argumentos a una función utilizando el nombre del parámetro en lugar de su posición. Esto permite que los argumentos se pasen en cualquier orden y mejora la legibilidad del código.



def print_full_name_with_default(name = "Sin nombre", surname = "Sin apellido", alias = "Sin alias"): ## Se puede poner un valor por defecto a un parámetro de una función. Si no se pasa un valor para ese parámetro, se utilizará el valor por defecto.  
    print(f"{name} {surname} {alias}")

print_full_name_with_default("Carlos", "Núñez",) ## Si no se pasa un valor para el parámetro 'surname', se utilizará el valor por defecto "Núñez". Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario proporcionar todos los argumentos cada vez que se llama a la función.
print_full_name_with_default("Carlos", "Núñez", "Pelucho") ## Si se pasa un valor para el parámetro 'surname', se utilizará ese valor en lugar del valor por defecto. Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario proporcionar todos los argumentos cada vez que se llama a la función.
  

def print_texts(*texts): ## El asterisco (*) antes del nombre del parámetro indica que la función puede aceptar un número variable de argumentos posicionales. Los argumentos se agrupan en una tupla llamada 'texts'. Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario proporcionar un número fijo de argumentos cada vez que se llama a la función.
        for text in texts:
             print(text.upper()) ## El método upper() se utiliza para convertir una cadena de texto a mayúsculas. Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario preocuparse por el caso de las letras al imprimir los textos.



 

print_texts("Hola", "Python", "Pelucho", "Flowmind2") ## Se pueden pasar varios argumentos a la función y se imprimirán uno por uno. Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario proporcionar un número fijo de argumentos cada vez que se llama a la función.
print_texts("Hola")



def weight_of_object (mass, gravity = 9.81):
    weight = float(mass * gravity) 
    print(f'Weight of an object in Newtons: {weight:.2f} N') 
    return weight
    
          
weight_object = weight_of_object(546546, 9.81)
print(weight_object)


def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling:", len(args))
    print(f"They are provided as a dictionary in my function:", type(args))
    print("Let's print them:") 
    for k, v in args.items():
         print(f"*Key: {k} \n Value: {v}\n")
         


arbitrary_named_args(name = "Carlos", surname = "Núñez", age = 14, country = "Spain") ## El doble asterisco (**) antes del nombre del parámetro indica que la función puede aceptar un número variable de argumentos con nombre. Los argumentos se agrupan en un diccionario llamado 'args'. Esto permite que la función sea más flexible y fácil de usar, ya que no es necesario proporcionar un número fijo de argumentos con nombre cada vez que se llama a la función.


def generate_team(team, *args):
     print(team)
     for player in args:
          print(player)

generate_team("Team A", "Juan Oterino", "Carlos Núñez", "Santiago Abascal", "Luis García")


# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York
# Se puede hacer de cualquier de las dos formas.
# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York



def square_number(n):
     result = n ** n
     return result    
def do_something(f,x):
     result_function = f(x)   ## f(x) es igual a decir square_number(x) , es decir , f es igual a square_number y x es igual a 3
     return result_function

resultado = do_something(square_number, 3)
print(resultado)  # Output: 27


def add_numbers(num_1,num_2):
     result = num_1 + num_2
     return result

total_sum = add_numbers(2,3)
print(total_sum)

import math

pi = math.pi

def area_circle(r):
     area = pi* r**2
     print(f"{area:.2f}")
     return area

total_area = area_circle(7)
print(total_area)


def add_all_nums(*nums):
     total = 0
     for numero in nums:
          total += numero
     return total
     
        
       

total_sum = add_all_nums(3,5,6,2,6)
print(total_sum)



def celcius_to_fahrenheit(num):
     formula = num*(9/5) + 32
     return formula

result = celcius_to_fahrenheit(40)
print(result)





def check_season(month):
     if month in["December","January","February"]:
          print("The season is Winter")
          
     elif month in["March","April","May"]:
          print("The season is Spring")
          
     elif month in["June","July","August"]:
               print("The season is Summer")
               
     elif month in["September","October","November"]:
               print("The season is Autumn")
               
     else:
          print("Te has equivocado, intentalo de nuevo")
     




check_season(input("Introduce el mes del año: ").capitalize())



def calculate_slope (*numbers):
     first_x_point = (float(input("Introduce el primer punto x: ")))
     first_y_point = (float(input("Introduce el primer segundo punto y: ")))
     second_x_point = (float(input("Introduce el segundo punto x: ")))
     second_y_point = (float(input("Introduce el segundo punto y: ")))
     return second_y_point - first_y_point/second_x_point-first_x_point

result=calculate_slope()
print(result)


def solve_quadratic_eq(a,b,c):
     formula = b**2 -4*a
     if formula >0:   
          x1 = (-b + formula**0.5)/2*a
          x2 = (-b - formula **0.5)/2*a
          return[x1,x2]
     elif formula == 0:
          x = (-b )/2*a
          return[x]
     else: 
          return[]


print(solve_quadratic_eq(1,5,5))


def print_list(*args):
     for element in args:
          print(element)
     return args

list = print_list("Carlos","Núñez","Patiño")
print(list)

def reverse_list(my_list):
    reversed_list = []
    for i in range(len(my_list)-1,-1,-1):
        reversed_list.append(my_list[i])
    return reversed_list

print(reverse_list([1,2,3,4,5]))


def capitalize_items(list):
    capitalized_items = []
    for item in list:
        capitalized_items.append(item.capitalize())
    return capitalized_items

my_second_list = capitalize_items(["carlos","nUÑEZ"])
print(my_second_list)


        
def print_list(list):
    my_list = []     
    for item in list:
        my_list.append(item)
        print(item)
    return my_list
   

my_first_list = print_list(["Carlos",14,1.80])
print(list)

sum_lists = my_first_list + my_second_list
print(sum_lists)


def add_item(list,item):
    list.append(item)
    return my_list

my_list = [1,2,3,4]
print(add_item(my_list,5))

def remove_item(my_list,item):
    my_list.remove(item)
    return my_list

list = ["Patata","Limón","Zanhaoria"]
print(remove_item(list,"Patata"))


def add_nums(number):
    total_sum = 0
    for i in range(number):
        total_sum += i
    return total_sum

print(add_nums(10))


def add_odd_nums(number):
    total_sum = 0
    for i in range(number):
          if i % 2 == 0:
              print()
          else:
               total_sum += i
    return total_sum
      
     

print(add_odd_nums(10))


def add_even_nums(number):
    total_sum = 0
    for i in range(number):
          if i % 2 == 0:
              total_sum += i
          
    return total_sum
      
     

print(add_even_nums(10))


def evens_and_odds (num):
    total_num_odds = 0
    total_num_evens = 0
    for i in range(num):
        if i % 2 == 0:
            total_num_evens += 1
        else:
            total_num_odds += 1
    return total_num_odds,total_num_evens


total = evens_and_odds(101)
print(total)


def factorial(number):
    factors = 1
    for i in range(1,number + 1):
        factors *= i
    return factors
    

result = factorial(5)
print(result)

def is_empty(check):
    if not check:
        print("Function is empty")
    else:
        print("Fucntion is correct")

print(is_empty(()))


def calculate_mean(list):
    result = 0
    division_num = len(list) 
    for i in list:
        result += i
    return result / division_num

mean = calculate_mean([1,5,9,10,3,5])
print(mean)

def calculate_median (list):
    sorted_list = sorted(list)
    numero = sorted_list
    par_o_impar = len(sorted_list)
    if par_o_impar % 2 == 0:
        result =(numero[par_o_impar//2-1],(numero[par_o_impar//2]))
        return result
    else:
        result_2 =(numero[par_o_impar//2])
        return result_2
    

total = calculate_median([1,7,2,34,2,5,1,7,7,3,9,2])
print(total)

def calculate_range(list):
    sorted_list = sorted(list)
    numbers = sorted_list
    range = numbers[-1] - numbers[0]
    return range

total = calculate_range([1,4,2,5,3,2,7,3])
print(total)


def calculate_mode(list):
    mode = {}
    for i in list:
        if i in mode:
          mode[i] += 1
        else:
            mode[i] = 1

    ordered_list = sorted(
        mode.items(),
        key= lambda item : item[1],
        reverse=True
        )

    for number,num in ordered_list[:1]:
        print(f"Mode = {number}")

result = calculate_mode([1,1,1,1,3,4,4,7,2])
print(result)



def calculate_variance(list):
    variance = list
    variance_list = []
    mean = 0
    division_number = len(list)
    elevated_numbers = []
    final_adition = 0
    for i in list :
        mean += i
    subtraction_number = mean / division_number
    for i in variance:
        paso_2 = i - subtraction_number
        variance_list.append(paso_2)
    for i in variance_list:
        elevated_numbers.append(i ** 2)
    for i in elevated_numbers:
        final_adition += i
        
    return final_adition/division_number

result = calculate_variance([1,4,2,5,3,6,3,7])
print(result)


def calculate_std(list):
    variance = list
    variance_list = []
    mean = 0
    division_number = len(list)
    elevated_numbers = []
    final_adition = 0
    for i in list :
        mean += i
    subtraction_number = mean / division_number
    for i in variance:
        paso_2 = i - subtraction_number
        variance_list.append(paso_2)
    for i in variance_list:
        elevated_numbers.append(i ** 2)
    for i in elevated_numbers:
        final_adition += i
    resultado_varianza = final_adition/division_number
    resultado_std = resultado_varianza ** 0.5
        
    return resultado_std

result_std = calculate_std([1,4,2,5,3,6,3,7])
print(result_std)

def greet (name = "Carlos"):
    print(f"{name}")

print(greet())

def show_args(**kwargs):
    return kwargs

result = show_args(name = "Carlos",surname="Núñez",age = 14,)
print(result)


    
def prime_num():
    prime_num = input("Introduce los numeros: ").split()
    for number in prime_num:
        number = int(number)
        is_prime = True
        if number < 2:
            is_prime = False
        else:
            for divisor in range(2,number):
                if number % divisor == 0:
                    is_prime = False
                  
        if is_prime:
            print(f"Number {number} is prime")
        else:
            print(f"Number {number} is not prime")
            

prime_num()


def unique_list(args):
    dict = {}
    
    for element in args:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    
    for item in dict.items():
        
        if item[1] > 1:
            is_unique = False
            break
        else:
            is_unique = True
            break
    if is_unique == True:
        print("The elements of the list are unique")
    else:
        print("The elements of the list are not uniques")

print(unique_list([1,1,2,3,4,5]))


def data_type (args):
    element_types = []
    for element in args:
        element_types.append(type(element))
    for types in element_types:
        if types == element_types[0]:
            are_same = True
        else:
            are_same = False
            break
    if are_same:
        print("The elements are the same type of data")
    elif not are_same:
        print("The elements are not the same type of data")

print(data_type([1,2,1,3]))









    


        
    


