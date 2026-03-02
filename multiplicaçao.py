"ola mundo"
# main.py

print("Mini Calculadora")

# Números já definidos
num1 = 8
num2 = 5

print(f"Soma: {num1} + {num2} = {num1 + num2}")
print(f"Subtração: {num1} - {num2} = {num1 - num2}")
print(f"Multiplicação: {num1} x {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Divisão: {num1} ÷ {num2} = {num1 / num2}")
else:
    print("Divisão: não é possível dividir por zero!")