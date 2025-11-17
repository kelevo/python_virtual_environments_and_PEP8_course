a = 0
b = 0

try:
    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa un numero: "))
    resultado = a / b
    print(f"Resultado: {resultado}")
except ValueError:
    print("El valor ingresado no es un numero")
except ZeroDivisionError:
    print("No esta permitido dividir por 0")