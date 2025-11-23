class DivisionError(Exception):
    """Error en la operacion"""
    pass



a = 0
b = 0

try:

    a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa un numero: "))

    if b == 2:
        raise DivisionError("No se puede dividir por 2")
    
    resultado = a / b
    print(f"Resultado: {resultado}")
    
except ValueError:
    print("El valor ingresado no es un numero")
except ZeroDivisionError:
    print("No esta permitido dividir por 0")
finally:
    print("Fin del programa")