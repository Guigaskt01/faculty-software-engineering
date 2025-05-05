"""3) Elaborar um algoritmo que recebe 3 valores (A, B e C) e exibe qual é o maior entre eles. 
Esse programa deve-se repetir 20 vezes."""

 
#Loop para solicitar 20 vezes 

for i in range(1,21,1): 

    A=int(input('Digite um valor para A:\n')) 

    B=int(input('Digite um valor para B:\n')) 

    C=int(input('Digite um valor para C:\n')) 

 

    #Encontrar maior valor com max() 

    maior=max(A,B,C) 

 

    #Exibe o maior valor 

    print(f'O Maior valor entre A= {A}, B= {B} e C= {C} é {maior}') 

 