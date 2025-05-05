"""Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada 
temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na 
tela. O programa termina quanto a temperatura inserida for menor que -5."""

# Solicita ao usuário uma temperatura em graus Celsius
grausCelsius = float(input('Digite um valor para temperatura em graus celsius: \n'))

# Enquanto a temperatura for maior ou igual a -5°C, o programa continua executando
while grausCelsius >= -5:    

    # Converte a temperatura de Celsius para Fahrenheit
    grausFahrenheit = (grausCelsius * (9 / 5)) + 32

    # Converte a temperatura de Celsius para Kelvin
    grausKelvin = grausCelsius + 273.15

    # Exibe os resultados das conversões
    print('--Conversor de temperatura--')
    print(f'Temperatura original (Celsius): {grausCelsius:.2f}°C')
    print(f'Temperatura convertida (Fahrenheit): {grausFahrenheit:.2f}°F')
    print(f'Temperatura convertida (Kelvin): {grausKelvin:.2f}°K')

    # Solicita nova temperatura para repetir ou encerrar o programa
    grausCelsius = float(input('Digite um valor para temperatura em graus celsius: \n'))

# Quando a temperatura for menor que -5°C, o programa encerra
print('Temperatura abaixo de -5°C. Programa encerrado.')



   
