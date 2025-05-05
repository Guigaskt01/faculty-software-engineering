"""6) Elaborar um programa que mostre ao usuário um menu com 4 opções de operações 
matemáticas (1- soma, 2- subtração, 3- multiplicação e 4- divisão). Após o usuário escolher uma 
das opções, o programa deve solicitar dois números e realiza a operação escolhida. Logo em 
seguida, o programa deve mostrar qual foi conta realizada e qual o resultad"""

#Exibe lista de operações para o usuário
print('Temos 4 opções de operações matemáticas.')
print('1-soma')
print('2-subtração')
print('3-multiplicação')
print('4-divisão')

#Solicita ao usuário sua escolha
escolha=(input('Qual voce tem interesse em utilizar ( selecione o numero ) ?'))

#Verifica a escolha do usuário
if escolha == '1':
    n1=float(input('Escreva um número'))
    n2=float(input('Escreva outro número'))
    soma=n1+n2

    #exibe valor da soma
    print(f'De acordo com sua escolha, o resultado da conta foi {soma:.2f}')

elif escolha == '2':
    n1=float(input('Escreva um número'))
    n2=float(input('Escreva outro número'))
    subtracao=n1-n2

    #Exibe valor da subtração
    print(f'De acordo com sua escolha, o resultado da conta foi {subtracao:.2f}')

elif escolha == '3':
    n1=float(input('Escreva um número'))
    n2=float(input('Escreva outro número'))
    multiplicacao=n1*n2

    #exibe valor da multiplicação
    print(f'De acordo com sua escolha, o resultado da conta foi {multiplicacao:.2f}')

elif escolha == '4':
    n1=float(input('Escreva um número'))
    n2=float(input('Escreva outro número'))
    divisao=n1/n2

    #Exibe valor da divisão 
    print(f'De acordo com sua escolha, o resultado da conta foi {divisao:.2f}')

#Entrada não existente exibe mensagem como "Inválido"
else:
    print('Entrada inválida, reinicie e escolha um número entre 1 a 4')









