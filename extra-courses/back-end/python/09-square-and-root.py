"""9) Elaborar um programa que receba um número positivo e maior que zero, calcule e mostre:
a) o número digitado ao quadrado;
b) a raiz quadrada do número digitado;"""

import math
#Esperar valor do usuário
numero_positivo=float(input('Digite um número maior que zero:\n'))

#valor digitado ao quadrado
numero_q=math.pow(numero_positivo, 2)

#Achar raiz quadrada do valor digitado
raiz=math.sqrt(numero_positivo)

#Exibir numero ao quadrado e raiz quadrada
print(f'O número ao quadrado ficou {numero_q:.2f} e sua raiz quadrada seria {raiz:.2f}')
