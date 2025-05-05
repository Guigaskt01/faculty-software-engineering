"""Elaborar um programa que receba o salário de um funcionário e o percentual de aumento,
 calcule e mostre o valor do aumento e o novo salário."""

#Esperar valores do usuário
salario=float(input('Digite seu salário:\n'))
percentual=float(input('Digite o percentual de aumento:\n'))

#achar o valor 
aumento=salario*(percentual/100)

novo_salario=salario+aumento

print(f'seu aumento foi de {aumento:.2f}, assim seu novo salário será {novo_salario:.2f}')