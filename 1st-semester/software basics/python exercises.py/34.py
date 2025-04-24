"""6) Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros.
 No final, o programa deve exibir quantos números são múltiplos de 3,
  quantos números são menores que 45 e maiores que 55, e qual é o menor número entre eles. """

 

#Cria listas para armazenar valores 

valores=[] 

menores_45=[] 

maiores_55=[] 

 

#Loop para solicitar valor 10 vezes 

for i in range(1,11,1): 

    num=int(input('Digite um valor:\n')) 

 

    #Verifica se número é multiplo de 3 

    if num % 3 == 0: 

        valores.append(num) 

    #Verifica se número é menor que 45 e maior que 55 

    if num < 45: 

        menores_45.append(num) 

    elif num > 55: 

        maiores_55.append(num) 

 

#Exibe lista com resultados 

print(f'Valores multiplos por 3, {valores}') 

print(f'números menores que 45{menores_45}') 

print(f'números maiores que 45{maiores_55}')