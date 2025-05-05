"""7) Elaborar um algoritmo que leia 10 números. Logo após,
 deve exibir o menor valor lido e o maior valor lido."""

#Cria lista para armazenar valores 
valores=[] 

 

#Loop para solicitar 10 vezes 

for i in range(1,11,1): 

    numeros=int(input('Digite um valor:\n')) 

    

    #Fornece valores para a lista com .append 

    valores.append(numeros) 

 

#Encontra menor valor dentro da lista 

menor_num=min(valores) 

 

#Encontra maior valor dentro da lista 

maior_num=max(valores) 

 

#Exibe menor e maior 

print(f'\nO menor valor digitado foi: {menor_num}')
print(f'O maior valor digitado foi: {maior_num}')