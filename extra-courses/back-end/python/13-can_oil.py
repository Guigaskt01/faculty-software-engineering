import math as m

# Elaborar um programa que receba o raio e a altura de uma lata de oleo para calcular basta apresentar o volume desta lata, dado. V=Pi*r2*h

# Esperar valores do usuário
raio = float(input('Digite o raio da lata de oleo:\n'))
altura = float(input('Digite a altura da lata de oleo:\n'))

# Achar o volume da lata de oleo
volume = m.pi * m.pow(raio, 2) * altura

#Exibir volume
print(f"De acordo com os dados fornecidos o volume é {volume:.2f}")