import math

#Elaborar um programa que receba um raio de esfera. O algoritimo deve calcular e exibir a área e o volume da esfera

#Espera o valor do usuário
raio=float(input('Digite o raio da esfera:\n'))

#Achar o volume e a area da esfera
volume=  (4/3) * math.pi * math.pow(raio,3)
area=  4 * math.pi * math.pow(raio, 2)

#Exibe area e volume
print(f'De acordo com o raio sua área é {area:.2f} e volume é {volume:.2f}')