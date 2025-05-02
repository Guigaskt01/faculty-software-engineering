"""Elaborar um programa que solicita um número (entre 10 a 15).
Se o usuário digitar um número diferente, o programa deve mostrar
a mensagem “Entrada inválida” e solicitar um número novamente.
Se digitar correto o programa deve mostrar a raiz quadrada desse número
e termina."""

import math

numero=int(input('Digite um número entre 10 a 15:\n'))

while numero < 10 or numero > 15:
    print('Entrada inválida')
    print('Tente novamente...')
    numero=int(input('Digite um número entre 10 a 15:\n'))

print(f'Valor Digitado: {numero}')
print(f'Raiz quadrada do valor: {math.sqrt(numero):.2f}')
