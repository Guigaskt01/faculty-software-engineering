"""7) Elaborar um programa que receba três valores (A, B, C). O programa deve verificar se eles 
podem ser valores dos lados de um triângulo, e se forem, se é um triângulo escaleno, equilátero 
ou isóscele, considerando os seguintes conceitos:
• O comprimento de cada lado de um triângulo é menor do que a soma dos outros
dois lados.
• Chama-se equilátero o triângulo que tem três lados iguais.
• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes
"""
#Solicita o valor de A para o usuário
valorA=int(input('Digite um valor para A'))

#Solicita o valor de B para o usuário
valorB=int(input('Digite um valor para B'))

#Solicita o valor de C para o usuário
valorC=int(input('Digite um valor para C'))

#Verifica se é possivel fazer um triangulo com os dados fornecidos
if (valorA < valorB + valorC) and (valorB < valorC + valorA) and (valorC < valorA + valorB):

    #Verifica se o triangulo é isósceles
    if (valorA == valorB) or (valorB == valorC) or (valorC == valorA):
        print('Seu triangulo é do tipo isósceles, possue dois lados iguais ')

    #Verifica se o triangulo é equilátero
    elif valorA == valorB == valorC:
        print('Seu triangulo é equilátero, possue três lado iguais')

    # Se não for nenhum dos dois, é escaleno
    else:
        print('Seu triangulo é escaleno, possue três lados com comprimentos diferentes')

#Não é possivel realizar um triangulo. Exibe mensagem como "Inválido"
else:
    print('Não é possivel formar um triangulo')