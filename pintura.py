# Programa para calcular área da parede e quantidade de tinta necessária

# Exemplo com números fixos
largura = 4.3   # largura da parede em metros
altura = 2.2    # altura da parede em metros

# Cálculo da área
area = largura * altura

# Cada litro de tinta pinta 2 m²
tinta_necessaria = area / 2

# Saída de resultados
print(f"A largura da parede é {largura} m.")
print(f"A altura da parede é {altura} m.")
print(f"A área da parede é {area:.1f} m².")
print(f"Será necessário {tinta_necessaria:.1f} litros de tinta para pintá-la.")
