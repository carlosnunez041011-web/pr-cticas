###Tuples

my_tuple = tuple()
my_other_tuple = (30, 60, 14)

my_tuple = (14, 1.80, "Carlos", "Núñez", "Carlos")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Carlos"))
print(my_tuple.index("Núñez"))
print(my_tuple.index("Carlos"))

'''my_tuple[1] = 1.90  #IndexError
print(my_tuple)'''  #No se puede cambiar un elemento porque una tupla es inmutable, solo puedes añadir o eliminar


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:7])
print(my_sum_tuple[:: -1])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Patiño"
print(my_tuple)

my_tuple.insert(1, "Azul")
print(my_tuple)

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

print("Carlos" in my_tuple)

del my_tuple
#print(my_tuple)NameError name 'my_tuple' is not defined porque el 'del' ha borrado la variable