"""Elaborar um programa que lê um número inteiro entre 1 e 7 e exibe o dia da semana 
correspondente. O programa deve repetir até que o usuário digite um número fora desse 
intervalo, caso isso aconteça o algoritmo mostra uma mensagem informando “Número 
inválido"""

# Solicita ao usuário um número de 1 a 7
numero = int(input('Digite um valor entre 1 e 7:\n'))

# Enquanto o número estiver no intervalo válido, executa o bloco
while 1 <= numero <= 7:
    # Verifica qual dia da semana corresponde ao número inserido
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
    
    # Solicita um novo número após mostrar o dia da semana
    numero = int(input('Digite um valor entre 1 e 7:\n'))

# Quando o número não estiver no intervalo, o programa sai do laço e exibe a mensagem
print('Número inválido, programa finalizado.')