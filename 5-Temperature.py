

def temperature():
    print("Patricia Núñez Patiño\n19/10/26")
    actual_temperature = int(input("Introduce the temperature in degrees Celsius: "))
    if actual_temperature < 10:
        print("It's cold")
    elif actual_temperature in range(10,26):
        print("It's a nice day")
    elif actual_temperature > 25:
        print("It's hot")

print(temperature())