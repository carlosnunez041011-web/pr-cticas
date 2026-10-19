### Sets

my_set = set()

my_other_set = {}

print(type(my_set))

print(type(my_other_set)) #Inicialmente es un diccionario

print(type(set(my_other_set)))

my_set = {1.88,"Flowmind2",56,"Carlos"}
my_other_set = {"Carlos","Núñez",14}


print(type(my_other_set)) #Es type set porque ya he introducido datos entre {}ç


print(len(my_other_set))

my_other_set.add("Flowmind2") #No es una estructura ordenada: {'Flowmind2', 'Núñez', 'Carlos', 14}

print(my_other_set)

my_other_set.add("Flowmind2") # Un set no admite repetidos

print(my_other_set)

print("Carlos" in my_other_set)

print("Patiño" in my_other_set)

my_other_set.remove("Carlos") 
print(my_other_set)

my_other_set.add("Carlos")
print(my_other_set)

todos_los_sets = my_other_set.union(my_set)

print(todos_los_sets)

comunes = my_other_set.intersection(my_set)
print(comunes)

diferencia = my_other_set.difference(my_set)
print(diferencia)

symetric_diference = my_other_set.symmetric_difference(my_set)
print(symetric_diference)



my_set = {"Carlos","Núñez",14}
my_list = list(my_set) ## No sirve pasarlo a lista porque sigue siendo aleatorio debido a que la lista se basa en el orden aleatorio del set
print(my_list)
print(my_list[1])



my_other_set = {1,2,3}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set)) ## No acepta repetidos