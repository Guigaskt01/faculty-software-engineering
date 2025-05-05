"""3) Elaborar um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa 
___________________________________________________________________________
|altura          |                     peso                                |
|--------------------------------------------------------------------------|
|                | até 60      entre 60 e 90 (inclusive)      acima de 90  |
|menor que 1,20  |    A                 D                         G        |
|de 1,20 a 1,70  |    B                 E                         H        |
|maior que 1,70  |    C                 F                         I        |
---------------------------------------------------------------------------|
"""

#Solicita a altura para o usuário.
altura=float(input('Digite sua altura (ex: 1.69):\n'))

#Solicita o peso para o usuário.
peso=float(input('Digite seu peso (em KG):\n'))

#Verifica qual será a classificação da pessoa, de acordo com a tabela.
if altura < 1.20: 
    if peso <= 60:
        classificacao='A' 
    elif peso < 60 and peso <= 90:
        classificacao='D'
    else:
        classificacao='G'

if altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        classificacao='B'
    elif peso < 60 and peso <= 90:
        classificacao='E'
    else:
        classificacao='H'

if altura > 1.70:
    if peso <= 60:
        classificacao='C'
    elif peso < 60 and peso <=90:
        classificacao='F'
    else:
        classificacao='I'

#Exibe a classificação de acordo com os dados fornecidos.
print(f'Sua classificação é {classificacao}')