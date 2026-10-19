num1 = float(input("Escribe el primer numero"))
operacion = input("Escribe la operacion que deseas realizar (+, -, *, /)")
num2 = float(input("Escribe el segundo numero"))

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    resultado = num1/num2
else:
    resultado = "Operacion no valida"

print("Resultado:", resultado)

