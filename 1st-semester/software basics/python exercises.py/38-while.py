""") Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana 
correspondente. O programa deve repetir até que o usuário digite um número fora desse 
intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número 
inválido"""

numero = int(input('Digite um valor entre 1 e 7:\n'))

while 1 <= numero <= 7:
    if numero == 1:
        print('Domingo')
    elif numero == 2:
        print('Segunda-feira')
    elif numero == 3:
        print('Terça-feira')
    elif numero == 4:
        print('Quarta-feira')
    elif numero == 5:
        print('Quinta-feira')
    elif numero == 6:
        print('Sexta-feira')
    elif numero == 7:
        print('Sábado')
    
    numero = int(input('Digite um valor entre 1 e 7:\n'))

# Fora do while (número inválido):
print('Número inválido, programa finalizando...')
