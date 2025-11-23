"""Typing con Python"""

# variable = valor
# variable: tipo = valor

variable = 42
print(f"Variable {variable} de tipo {type(variable)}")

variable = 200
print(f"Variable {variable} de tipo {type(variable)}")

otra_variable: int = 20
print(f"Variable {otra_variable} de tipo {type(otra_variable)}")

user_id: int | None = None
print(f"Variable {user_id} de tipo {type(user_id)}")