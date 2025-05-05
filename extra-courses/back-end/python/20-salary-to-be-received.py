'''Elaborar um programa que receba o número de horas trabalhadas e o valor do salário mínimo.
Calcule e mostre o salário a receber seguindo as regras abaixo:
a)O valor da hora trabalhada vale a metade do salário mínimo:
b)O salário bruto equivale ao número de horas trabalhadaas multiplicado pelo valor da hora 
c)O imposto equivale a 3% do salário bruto:
d)O salário a receber equivale ao salário bruto menos o imposto
'''

horas_trabalhadas=float(input('Digite a quantidade de horas trabalhadas:\n'))
salario_minimo=float(input('Digite o salário minímo atual:\n'))

valor_hora=(salario_minimo/2)/220
salario_bruto=horas_trabalhadas*valor_hora
imposto=salario_bruto*0.03
salario_receber=salario_bruto-imposto

# Saída de resultados
print('\n--- Cálculo do Salário ---')
print(f'Valor da hora trabalhada: R$ {valor_hora:.2f}')
print(f'Salário bruto: R$ {salario_bruto:.2f}')
print(f'Imposto (3%): R$ {imposto:.2f}')
print(f'Salário a receber: R$ {salario_receber:.2f}')