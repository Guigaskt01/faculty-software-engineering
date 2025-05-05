"""Elaborar um programa que solicita um número (entre 10 a 15).
Se o usuário digitar um número diferente, o programa deve mostrar
a mensagem “Entrada inválida” e solicitar um número novamente.
Se digitar correto o programa deve mostrar a raiz quadrada desse número
e termina."""

import math  # Importa o módulo math para usar funções matemáticas

# Solicita ao usuário um número entre 10 e 15
numero = int(input('Digite um número entre 10 a 15:\n'))

# Enquanto o número estiver fora do intervalo, pede novamente
while numero < 10 or numero > 15:
    print('Entrada inválida')
    print('Tente novamente...')
    numero = int(input('Digite um número entre 10 a 15:\n'))

# Mostra o valor digitado
print(f'Valor Digitado: {numero}')

# Calcula e exibe a raiz quadrada formatada com duas casas decimais
print(f'Raiz quadrada do valor: {math.sqrt(numero):.2f}')
