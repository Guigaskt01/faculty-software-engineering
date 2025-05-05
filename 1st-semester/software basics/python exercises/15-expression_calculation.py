"""15) Elaborar um programa que leia três números inteiros (A, B, C) e calcule a seguinte expressão:
D=R + S/2 onde R=(A+B)² e S=(B+C)². Exibir o resultado da expressão D."""

# Esperar os valores dos números inteiros A, B e C
a = int(input('Digite o valor de A:\n'))
b = int(input('Digite o valor de B:\n'))
c = int(input('Digite o valor de C:\n'))

# Calcular R e S
r = (a + b) ** 2
s = (b + c) ** 2

# Calcular D
d = r + s / 2

# Exibir o resultado da expressão D
print(f'O resultado da expressão D é: {d:.2f}')