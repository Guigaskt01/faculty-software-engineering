import math
#10) Elaborar um programa que dados dois lados de um triângulo retângulo calcule e exiba a respectiva hipotenusa.

#Esperar valores do usuário
lado1=int(input('Digite um número:\n'))
lado2=int(input('Digite um número:\n'))

#Encontrar hipotenusa do triângulo
hipot=math.hypot(lado1,lado2)

#Exibir hipotenusa do triângulo
print(f'A hipotenusa do triangulo retangulo é {hipot:.2f}')

