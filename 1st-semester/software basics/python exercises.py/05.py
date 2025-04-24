#Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.

#Esperar valor do usuário
saldo=float(input('Digite seu saldo :\n'))

#Encontrar o valor do reajuste
reajuste=saldo*(15/100)

#Somar saldo com o valor do reajuste achando novo salario
novo_saldo=saldo+reajuste

#Exibir novo saldo
print(f'Novo saldo é {novo_saldo:.2f}')