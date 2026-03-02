#Programa completo para calcular a média de notas

# Primeiro, o tradicional "Olá Mundo"
print("Olá Mundo!")

# Notas já definidas
nota1 = 8.0
nota2 = 7.5
nota3 = 9.0
nota4 = 6.5

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe as notas e a média
print("Notas:", nota1, nota2, nota3, nota4)
print(f"A média das notas é: {media:.2f}")

# Verifica se o aluno foi aprovado (considerando média >= 7)
if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")

