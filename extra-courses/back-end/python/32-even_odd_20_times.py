"""4) Elaborar um algoritmo que lê 20 números inteiros. 
Para cada número inserido exibir se é par ou ímpar. """

#Loop para solicitar 20 vezes 

for i in range(1,21,1): 

    num=int(input('Digite um valor:\n')) 

    #Verificar se é par ou ímpar 

    if num % 2 == 0: 

        print ('Número par') 

    else: 

        print('Número impar')