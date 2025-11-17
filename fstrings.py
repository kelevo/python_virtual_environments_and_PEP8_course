from datetime import datetime

name = "Ana"
year = 2020
text = f"Hola {name}"
print(text)


text_suma = f"Hola {name}, tu edad es: {2025 - year}"
print(text_suma)


text_function = f"HOLA {name.upper()}"
print(text_function)


edad = 20
text_if = f"Hola {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad"
print(text_if)


bank_balance = 1200000000
text_bank_balance = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text_bank_balance)


stock_price = 1.405
text_stock_price = f"El valor del stock es: {stock_price:.1f}"
print(text_stock_price)


user_id = 1
text_user_id = f"Su id es: {user_id:03d}"
print(text_user_id)


product = "Laptop"
price = 1000
text_product = f"Producto: {product:>15} | Precio: {price}"
print(text_product)
print(f"{text_product}\n{text_product}")


date = datetime(2024, 12, 5, 10, 10)
text_datetime = f"La fecha es: {date: %A %d de %Y a las %I:%M %p}"
print(text_datetime)