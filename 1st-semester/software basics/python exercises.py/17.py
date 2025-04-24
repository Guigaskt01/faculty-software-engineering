'''Elaborar um programa que leia a idade de uma pessoa expressa em anos, 
meses e dias e mostre-a expressa apenas em dias'''

anos = int(input("Quantos anos completos você tem? "))
meses = int(input("Quantos meses se passaram desde o último aniversário? "))
dias = int(input("E além disso, quantos dias se passaram desde o último mês completo?"))

total_dias=(anos*365)+(meses*30)+ dias

print(f'Sua idade total em dias é : {total_dias} dias.')