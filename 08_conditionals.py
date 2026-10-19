### Conditionals 

my_condition = True

if my_condition:    ### if my_condition: es lo mismo que if my_condition == True
    print("Se ejecuta la condicion del if")


my_condition = 5 * 5

if my_condition == 10 :    ### if my_condition: es lo mismo que if my_condition == 10
    print("Se ejecuta la condicion del segundo if")



elif my_condition > 10 and my_condition < 20:
    print("Es mayor que diez y menor que 20")   
elif my_condition == 25:
    print("Es igual a 25")   
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")


print("La ejecución continúa")


##my_string = True    if not my_string = False


my_string = ""    ## Si tenemos un str vacío , el 'if' nos lo da como False y no se imprime

if not my_string:   ### Estoy negando la condición de que my_string este vacía
    print("Mi cadena de texto es vacía")


if my_string == "Mi cadena de texto":
    print("Estas cadenas de texto coinciden")


if my_string == "Mi cadena de texto0000":      ## Este caso no se cumple
    print("Mi cadena de no texto es vacía")





my_age = int(input("Enter my age: "))

years_left_to_drive = 18 - my_age

if my_age < 18 :
    print(f"You need to be {years_left_to_drive} years older to learn how to drive")
elif age == 18:
    print("At the limit but your allowed to drive")
else:
    print("Your allowed to drive")


your_age = int(input("Enter your age: "))

my_age_difference = my_age - your_age
your_age_difference = your_age - my_age

if my_age > your_age:
    print(f"I'm {my_age_difference} years older than you")
else:
    print(f"Your {your_age_difference} years older than me")



num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 == num_2:
    print(f"{num_1} is the same as {num_2}")
else:
    print(f"{num_1} is smaller than {num_2}")



grade = float(input("Enter your grade: "))

if grade < 49:
    print("F")
elif grade >= 49 and grade < 59 :
    print("D")
elif grade >= 59 and grade < 69 :
    print("C")
elif grade >= 69 and grade < 79 :
    print("B")
elif grade >= 79 and grade < 89 :
    print("A")
elif grade >= 89 and grade <= 100 :
    print("A+")



fruits_list = []
respuesta = "si"



while respuesta in ["si","sí"]:

    fruit = input("Enter fruit: ").capitalize()

    if fruit not in fruits_list:
        fruits_list.append(fruit)

        print(fruits_list)

    else: # or elif
        print(fruits_list)

    respuesta = input("Do you want to add another fruit?: ")


print(f"The fruits list is: {fruits_list} ")


person={
     'first_name': 'Asabeneh',
     'last_name': 'Yetayeh',
     'age': 250,
     'country': 'Finland',
     'is_married': True,
     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address': {
            'street': 'Space street',
            'zipcode': '02210'
                                }
                    }

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



if "skills" in person.keys():
    print(person['skills'][3])


if "Python" in person["skills"]:
    print("Python esta en skills")


skills = person["skills"]

if "JavaScript" in skills and "React" in skills:
    print("He is a front developer")
elif 'Node' in skills and 'MongoDB' in skills and 'Python' in skills:
    print("He is a backend developer")
elif "React" in skills and "Node" in skills and "MongoDB" in skills:
    print("He is a fullstack developer")
else:
    print("Unknown title")


person_name = input("What is your first name?: ").capitalize()
person_location = input("Where do you live?: ").capitalize().strip()
is_married = input("Are you married?: ").lower().strip()


if person_location in ["Finland"] and is_married in ["yes"]:
    print(f"{person_name} lives in {person_location}. He is married")
else:
    print("Incorrect description")



                
      
                






