"""Elaborar um programa que lê um número N inteiro maior que 2 
(caso N não for maior que 2 deve solicitar outro número).
Logo após o programa deve exibir o quadrado e o cubo de 2 até N"""

import math

numero=int(input('Digite um número acima de 2:\n'))

while numero < 2:
    print('número inválido, tente novamente...')

    numero=int(input('Digite um número acima de 2:\n'))

for i in range(2,numero +1):
    quadrado=math.pow(numero, 2)
    cubo=math.pow(numero, 3)

print(f'O valor fornecido é {numero}')
print(f'Valor fornecido ao quadrado: {quadrado:.2f}')
print(f'Valor fornecido ao cubo : {cubo:.2f}')