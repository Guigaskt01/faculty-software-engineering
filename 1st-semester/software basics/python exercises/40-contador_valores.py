"""Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar 
o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80, 
quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário"""

# Listas para armazenar os números em diferentes categorias
acima_80 = []
abaixo_10 = []
valores = []

# Começa com um valor diferente de 100 para entrar no laço
numero = 0

# Enquanto o número digitado for diferente de 100, continua pedindo valores
while numero != 100:
    numero = int(input('Digite um número, ou 100 para encerrar: '))

    # Só entra no processamento se o número for diferente de 100
    if numero != 100:
        valores.append(numero)  # Adiciona à lista geral

        if numero > 80:
            acima_80.append(numero)
        elif numero < 10:
            abaixo_10.append(numero)

# Após o loop, calcula soma e média apenas se houver valores
if valores:
    soma = sum(valores)
    media = soma / len(valores)

    print(f'Valores acima de 80: {len(acima_80)}')
    print(f'Valores abaixo de 10: {len(abaixo_10)}')
    print(f'A média é {media:.2f}')
else:
    print('Nenhum número válido foi digitado.')
