### Loops

## While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
if my_condition == 10:                        
    print("Mi condicion es igual a 10")
elif my_condition == 10:
    print("Mi condicion es igual a 10")
else:
    print("Mi condición es mayor que 10") ## Cuando esta sin el if dentro del while, se cumple, pero al ponerle el if, ya no se cumple


print("La ejecución continúa")

my_condition = 0

while my_condition < 20:
     my_condition += 1
     if my_condition == 15:
         print("Se detiene la ejecución")
         break
     print(my_condition)

print("La ejecución continúa")


## For

my_list = [35 , 24 , 62 , 52 , 30 , 30 , 17]

for element in my_list:
    print(element)

my_tuple = (14, 1.80, "Carlos", "Núñez", "Carlos")

for element in my_tuple:
    print(element)

my_set = {1.88,"Flowmind2",56,"Carlos"}

for element in my_set:
    print(element)

my_dict = { 
    "Nombre":"Carlos",
    "Apellido":"Núñez",
    "Edad":14,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.88
    }

for element in my_dict.values():
    print(element)


for element in my_dict: ## En el momento que le metemos un for a dict, se imprimen solo los keys(claves)
    print(element)
    if element == "Edad":
        break
    elif element == "Apellido":
        print(f"Su apellido es: {my_dict['Apellido']}")

else:     ## Este 'else' cuando rompemos el 'for' , ya no aparece
    print("El bucle for para mi diccionario ha finalizado") 



print("La ejecución continua")


my_dict = { 
    "Nombre":"Carlos",
    "Apellido":"Núñez",
    "Edad":14,
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.88
    }

print(my_dict.items())

for key, value in my_dict.items():
    print(key,":", value)


for element in my_dict: 
    print(element)
    if element == "Edad":
        continue ## El continue , continua pero saltandose todo lo que venga dspues en el bucle y volviendo al principio del 'for'
    elif element == "Apellido":
        print(f"Su apellido es: {my_dict['Apellido']}")
    print("Se ejecuta")

else:     ## Este 'else' cuando rompemos el 'for' , ya no aparece
    print("El bucle for para mi diccionario ha finalizado")


count = 0
while count < 5:
    if count == 3:
        count += 1  
        continue
        
    print(count)
    count = count + 1




my_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_new_condition = 0

while my_new_condition <= 10 :

    print(my_new_condition)
    my_new_condition += 1


    

    


for numbers in my_nums:
    print(numbers)



for numbers in reversed(my_nums):
    print(numbers)




for number in range(1, 8):
    print("#" * number)
    if number in range(2,3):
        print("Se termina la ejecución")
        break



num_1 = 0
num_2 = 0
total_num = num_1 * num_2

while num_1 <= 10 and num_2 <= 10:
    print(f"{num_1} * {num_2} = {total_num}")
    num_1 += 1
    num_2 += 1
    total_num = num_1 * num_2


for fila in range(8):
    for columna in range(8):
        print(" Carlos ", end=" ")  # end= "\n "  baja de línea, es el valor normal                                   #
    print()                         # end= " " añade un espacio y sigue en la misma linea
                                    # end= "" no añade nada
                                    #end= "-" añade un guión
                                    #print() añade un espacio vacio al final de cada fila 


skills =  ['Python', 'Numpy','Pandas','Django', 'Flask']

for skill in skills:
    print(skill)


for numero in range(101):
    if numero % 2 == 0:
        print(numero)
    else:
        print()


for numero in range(101):
    if numero % 2 == 0:
        print()
    else:
        print(numero)

suma_total = 0


for numero in range(101):
    suma_total += numero
    print(numero)

print(f"La suma total de los números es {suma_total}")

suma_pares = 0
suma_impares = 0

for numero in range(101):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero
    print(numero)

print(f"La suma total de los numeros pares es: {suma_pares}")
print(f"La suma total de los numeros impares es: {suma_impares}")



countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]




for countrie in countries:
    if "land" in countrie:
        print(countrie)


fruit_list = ['banana', 'orange', 'mango', 'lemon']

for fruit in reversed(fruit_list):
    print(fruit)






        






