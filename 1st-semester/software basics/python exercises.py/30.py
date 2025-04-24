"""2) Elaborar um algoritmo que leia um número inteiro e mostre uma mensagem indicando
se este número é múltiplo de 3 e se é positivo ou negativo.
 Esse programa deve-se repetir 6 vezes esse processo.""" 

 

#Loop para  solicitar 6 vezes 

for c in range(1,7,1): 

    num_int=int(input('Digite um número:\n')) 

 

    #Verificar se número é multiplo por 3 

    if num_int % 3 == 0: 

 

        #Verificar se número é positivo 

        if num_int >= 0: 

            print('Este número é Múltiplo por 3 e também é um número Positivo') 

        else: 

            print('Este número é Múltiplo por 3 e também é um número negativo') 

    else: 

        print('Não é divisivel por 3') 