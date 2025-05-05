'''
Elaborar um programa que calcule o salário líquido de um  funcionário,
exibindo no final o nome, telefone e o salário líquido, considerando:
a)Os dados do funcionário:nome,RG e telefone.
b)Salário bruto de R$ 2500,00
c)Descontos de R$ 300,00
'''
nome=input('Informe seu nome:\n')
RG=input('Informe seu RG (apenas números):\n')
telefone=input('Informe seu número de telefone (com DDD):\n')

salario_bruto=2500.00
descontos=300.00

salario_liquido=salario_bruto-descontos

print('\n--Dados funcionário--')
print(f'{nome}')
print(f'{RG}')
print(f'{telefone}')
print(f'Salário líquido: R${salario_liquido:.2f}')