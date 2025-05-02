"""Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada 
temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na 
tela. O programa termina quanto a temperatura inserida for menor que -5."""


grausCelsius=float(input('Digite um valor para temperatura em graus celsius: \n'))

while grausCelsius >=-5:    

    grausFahrenheit=((grausCelsius*(9/5))+32)

    grausKelvin=(grausCelsius+273.15)

    print('--Conversor de temperatura--')
    print(f'temperatura original (Celsius): {grausCelsius:.2f}°C')
    print(f'temperatura convertida (Fahrenheit): {grausFahrenheit:.2f}°f')
    print(f'temperatura convertida (Kelvin): {grausKelvin:.2f}°K')

    grausCelsius=float(input('Digite um valor para temperatura em graus celsius: \n'))

print('Temperatura abaixo de -5°C. Programa encerrado.')


   
