"""Elaborar um programa que lê um número N inteiro maior que 2 
(caso N não for maior que 2 deve solicitar outro número).
Logo após o programa deve exibir o quadrado e o cubo de 2 até N"""

import math

# Solicita um número maior que 2
numero = int(input('Digite um número acima de 2:\n'))

# Verifica se o número é menor que 2 e repete até ser válido
while numero <= 2:
    print('Número inválido, tente novamente...')
    numero = int(input('Digite um número acima de 2:\n'))

# Exibe o quadrado e o cubo de 2 até N
print(f'Quadrado e cubo dos números de 2 até {numero}:')
for i in range(2, numero + 1):
    quadrado = math.pow(i, 2)
    cubo = math.pow(i, 3)
    print(f'Número {i}: Quadrado = {quadrado:.2f}, Cubo = {cubo:.2f}')