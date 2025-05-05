#14) Elaborar um programa que leia uma temperatura em graus Celsius e deve converter em graus

#Fahrenheit. A fórmula de conversão é: F = (9*C+160)/5, sendo F a temperatura em Fahrenheit e C

#a temperatura em Celsius. Exibir a temperatura em Fahrenheit.

# Esperar o valor da temperatura em Celsius
celsius = float(input('Digite a temperatura em Celsius:\n'))

# Converter Celsius para Fahrenheit
fahrenheit = (9 * celsius + 160) / 5

# Exibir a temperatura em Fahrenheit
print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}')