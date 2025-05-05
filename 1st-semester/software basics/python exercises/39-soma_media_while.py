"""Elaborar um programa que deve ler N números. Caso o usuário digite zero (0), o programa 
deve exibir a somatória e a média dos valores inseridos"""

# Cria uma lista para armazenar os números digitados
armazenarNumeros = []

# Solicita ao usuário que digite um número
numero = float(input('Digite um número:\n'))

# Enquanto o número digitado for maior que 0, ele será armazenado
while numero > 0:
    armazenarNumeros.append(numero)  # Adiciona o número à lista
    numero = float(input('Digite um número:\n'))  # Solicita outro número

# Quando o usuário digita 0, o programa calcula a soma e a média

# Soma todos os números da lista
somar = sum(armazenarNumeros)

# Calcula a média dividindo a soma pela quantidade de números
media = somar / len(armazenarNumeros)

# Exibe os resultados
print(f'Soma: {somar}')
print(f'Média: {media}')
