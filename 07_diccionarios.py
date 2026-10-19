## Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_other_dict))

my_other_dict = {"Nombre":"Carlos", "Apellido":"Núñez", "Edad":14, 1:"Python"} ## Version simple

my_dict = { ##Versión compleja(la mejor)
    "Nombre":"Carlos",
    "Apellido":"Núñez",
    "Edad":14,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.88
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Mario"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Río Tajuña 8"  ## Agregar un nuevo campo al diccionario
print(my_dict)

del my_dict["Calle"]
print(my_dict)

my_dict.get("Nombre")
print(my_dict)

my_dict["Lenguajes"].add("JavaScript")
print(my_dict)

my_dict["Lenguajes"].remove("JavaScript")
print(my_dict)

print(len(my_dict))

print(my_dict.get("email","No disponible"))

if "Nombre" in my_dict:
    print("Existe la clave nombre")
    print(f"El nombre de la persona es {my_dict["Nombre"]}")


print("Nombre" in my_dict)
print(my_dict.keys()) ## dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print(my_dict.values()) ##dict_values(['Mario', 'Núñez', 14, {'Kotlin', 'Python', 'Swift'}, 1.88])
print(my_dict.items()) ##dict_items([('Nombre', 'Mario'), ('Apellido', 'Núñez'), ('Edad', 14), ('Lenguajes', {'Kotlin', 'Python', 'Swift'}), (1, 1.80)

my_list = ["Nombre", 1,"Piso"]

my_new_dict = dict.fromkeys(my_list) ## {'Nombre': None, 1: None} Crea un diccionari sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1,"Piso")) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,("Carlos","Núñez")) 
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,my_dict)    ###El valor que vaya despues de la ',' de my_dict , correspondera a cada clave de ldiccionario
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))


my_new_dict = dict.fromkeys(my_dict,["Carlos","Núñez"]) 
print(my_new_dict)
print(list(my_new_dict))
print(set(my_new_dict))
print(tuple(my_new_dict))
print(list(dict.fromkeys(list(my_new_dict.keys()))))


empresa = {
    "Nombre_empresa":"Flowmind2",
    "Dirección": {
    "Ciudad":"Madrid",
    "Código postal":28001
    }
}

print(empresa["Nombre_empresa"])
print(empresa["Dirección"]["Ciudad"])
print("Nombre_empresa" in empresa)







dog = {
    "Bread":"Pitbull",
    "Color":"Black and brown",
    "Age": 7
}

print(dog)



student = {
    "First name":"Carlos",
    "Last name":"Núñez",
    "Gender":"Male",
    "Age":14,
    "Skills":["Skiing","Python","JavaScript"],
    "Country":"Spain",
    "City":"Madrid",
    "Adress":int("02130")
}

print (student)

print(student.keys())
print(student.values())

tuple = student.items()
print(tuple)

del student["First name"]
print(student)

del student