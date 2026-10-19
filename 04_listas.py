# Listas
# El fichero de listas , es decir este , es muy importante para la inteligencia artificial

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35 , 24 , 62 , 52 , 30 , 30 , 17]

print(my_list)
print(len(my_list))
print(my_list[4])


my_other_list = [35, 1.81, "Carlos", "Núñez"] # No hace falta que en la lista [] , guardemos esl mismo tipo de dato

print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count("Núñez")) #El .count puede servir para contar datos repetidos como en my_list el numero 30 está repetido
print(my_other_list.count(35))
print(my_list.count(30))
print(len(my_other_list[2])) # Esto cuenta el numero de caracteres de los propios elementos dentro de las listas
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
print(len(str(my_other_list[0])))# Solo se puede contar los caracteres de los string

age, height, name, surname  = my_other_list # La variable la podemos llamar como queramos pero tiene que ser coherente con el elemento y tiene que estar en orden por ejemplo si yo cambio el orden a height y a age , el sistema no va a saber que 1.81 es el height

print(name) 
print(len(str(height)))
#Complicarse de mas , no hace falta hacerlo
name, height, age, surname  = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list) IndexError

my_other_list.append("Flowmind2")#Con la operacion append , se añade uno o varios elementos al final de la lista
print(my_other_list)

my_other_list.insert(1, "Azul")#Con la operacion insert, se inserta un elemento a la posicion elegida
print(my_other_list)

my_other_list[1] = "Rojo"
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)


my_list.remove(30)#En este caso , hay dos 30 pues solo se elimina el primero que aparezca en el codigo
print(my_list)


print(my_list.pop())#Inserta o quita ciertos elementos
print(my_list)


my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

del my_list#El del es para eliminar un elemento de la lista sin guardarselo
print(my_new_list.copy)


my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_new_list.sort(reverse=True)
print(my_new_list)

print(my_new_list[1:2])



my_list = "Hola Python"
print(my_list)
print(type(my_list))

my_list = ["Hola Python"]
print(my_list)
print(type(my_list))

del my_list
#print(my_list) NameError: name 'my_list' is not defined
print(my_list)





