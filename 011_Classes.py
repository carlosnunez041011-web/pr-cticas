###Classes
class MyEmptyPerson:  ## Los nombres de las clases , se escriben con mayuscula la primera
    pass

print(MyEmptyPerson())

class Person:
    def __init__(self,name,surname,alias = "Sin alias"):  ## No es una funcion debido al init self , es un lugar donde podemos establecer ciertos valores asociados a Person
        #self.name = name              ## He almacenado los datos(parametros) en el self.(valor que yo le de)
        #self.surname = surname        ## No es necesario poner parametro si pones el self.name = "Carlos" porque ya esataria definido dentro del constructor
        self.full_name = (f"{name} {surname} ({alias})")#Propiedad pública
        self._name = name  #Propiedad privada

    def get_name(self):
        return self._name
        
    def walk (self):
        print(f"{self.full_name} esta caminando")
            


my_person = Person("Carlos","Nuñez")
print(my_person.full_name)
my_person.walk()


my_other_person = Person("Brais","Moure","Mouredev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)" ## Buscar explicacion al porque le he podido cambiar el valor a full_name
print(my_other_person.full_name)


my_other_person.full_name = 666
print(my_other_person.full_name)

my_other_person = Person("Carlos","Núñez","Macho")
print(my_other_person.full_name)

print(my_other_person.get_name())


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


class Statisitics:
    def __init__(self,datos):
        self.datos = datos
        self.count = 0
        self.sum = 0
        self.numero_mas_bajo = 0
        self.numero_mas_alto = 0
        self.frecuency_distribution = {}
    def contar(self):
        self.count = 0
        for i in self.datos:
            self.count +=1
        return self.count
    def sumar(self):
        self.sum = 0
        for i in self.datos:
            self.sum += i
        return self.sum
    def num_mas_bajo(self):
        
        self.numero_mas_bajo= sorted(
            self.datos
            )
        for i in self.numero_mas_bajo[:1]:
            self.numero_mas_bajo = i
        return self.numero_mas_bajo
    def num_mas_alto(self):
        self.numero_mas_alto = sorted(
            self.datos,
            reverse=True
        )
        for i in self.numero_mas_alto[:1]:
            self.numero_mas_alto = i
        return self.numero_mas_alto
    def freq_distribution(self):
        self.frecuency_distribution = {}
        for i in self.datos:
            if i in self.frecuency_distribution:
                self.frecuency_distribution[i] += 1
            else:
                self.frecuency_distribution[i] = 1
        ordered_list = sorted(
                self.frecuency_distribution.items(),
                key= lambda item : item[1],
                
                )
        
        new_list = []
        for number,num in ordered_list:
            new_list.append(f"{number}:{num}")
        return new_list

data = Statisitics(ages)
print(data.datos)
print(data.contar())
print(data.sumar())
print(data.num_mas_bajo())
print(data.num_mas_alto())
print(data.freq_distribution())



class PersonAccount:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.income = []
        self.expenses = []
    def add_income (self,amount,description):
        self.income.append([amount,description])
        return self.income
    def add_expenses (self,amount,description):
        self.expenses.append([amount,description])
        return self.expenses
    def total_income(self):
        total = 0
        for income in self.income:
            total += income[0]
        return total
    

carlos = PersonAccount("Carlos","Núñez")
print(carlos.add_income(100,"Venta de esquís"))
print(carlos.add_income(45,"Reventa de zapatillas"))
print(carlos.add_expenses(50,"Transporte"))
print(carlos.total_income())

##EXPLICAR EN VOZ ALTA EL PROYECTO 1 COMO SI ESTUVIERA DANDO UNA CLASE