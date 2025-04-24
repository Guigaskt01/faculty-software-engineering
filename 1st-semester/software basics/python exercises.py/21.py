"""
1) Elaborar um programa que leia a idade e o tempo de serviço de um trabalhador e mostre se o 
trabalhador pode ou não se aposentar. As condições para aposentadoria são:

• Ter pelo menos 65 anos

• Ou ter trabalhado pelo menos 30 anos

• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 ano
"""

#Solicita idade
idade=int(input('Digite sua idade'))

#Solicita tempo de serviço 
tempo_serviço=int(input('Digite seu tempo de serviço (em anos): ?'))

#Verifica se é possivel se aposentar 
if idade >= 65 or tempo_serviço >= 30 or (idade >60 and tempo_serviço >= 25):
    print('Você pode se aposentar')
else:
    print('Você ainda não pode se aposentar')