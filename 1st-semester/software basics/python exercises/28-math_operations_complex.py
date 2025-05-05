"""8) Elaborar um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo a letra digitada pelo usuário

a) Geométrica -> 3raiz x*y*z
b) Ponderada  -> x+2*y+3*z
c) Harmônica  -> 1/ (1/x) + (1/y) + (1/z)
d) Aritmética -> x+y+z/3
"""

import math

#Exibe uma lista de opções para o usuário escolher.
print('a) Geométrica')
print('b) Ponderada')
print('c) Harmônica')
print('d) Aritmética')

#Solicita a escolha do usuário.
escolha=(input('Escolha uma letra para utilizar as funções de dentro dela\n'))

#Verifica a escolha do usuário e ínicia a conta da opção
if escolha == 'a':

    x=int(input('De um valor para X '))
    y=int(input('De um valor para Y '))
    z=int(input('De um valor para Z '))
    mult=x*y*z
    geometrica=math.pow(mult, 1/3)

    print(f'De acordo com sua escolha, o resultado da conta foi {geometrica:.2f}')

elif escolha == 'b':

    x=int(input('De um valor para X '))
    y=int(input('De um valor para Y '))
    z=int(input('De um valor para Z '))
    ponderada=(x + 2 * y + 3 * z) / 6

    print(f'De acordo com sua escolha, o resultado da conta foi {ponderada:.2f}')

elif escolha == 'c':

    x=int(input('De um valor para X '))
    y=int(input('De um valor para Y '))
    z=int(input('De um valor para Z'))
    harmonica = 3 / ((1/x) + (1/y) + (1/z))

    print(f'De acordo com sua escolha, o resultado da conta foi {harmonica:.2f}')

elif escolha == 'd':

    x=int(input('De um valor para X '))
    y=int(input('De um valor para Y '))
    z=int(input('De um valor para Z'))
    aritmetica = (x + y + z) / 3

    print(f'De acordo com sua escolha, o resultado da conta foi {aritmetica:.2f}')

#Entrada não existente exibe mensagem como "Inválido"
else:
    print('Entrada inválida, reinicie e escolha entre a até d')