"""Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar 
o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80, 
quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário"""

acima_80=[]

abaixo_10=[]

valores=[]

contador= 0

numero=0

while numero != 100:

    numero=int(input('Digite um número, ou 100 para encerrar: '))
    contador += 1
    if numero == 100:
        print('Encerrando programa...')
    elif numero > 80:
        valores.append(numero)
        acima_80.append(numero)
    elif numero < 10:
        valores.append(numero)
        abaixo_10.append(numero)
    else:
        valores.append(numero)

soma=sum(valores)
media=soma/len(valores)

print(f'Valores acima de 80: {len(acima_80)}')
print(f'Valores abaixo de 10: {len(abaixo_10)}')
print(f'A media é {media:.2f}')