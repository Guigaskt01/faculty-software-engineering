"""5) Elaborar um algoritmo que solicita ao usuário para digitar 15 valores
e deve exibir a soma e média. """

 

#Criar lista para armazenar 

valores=[] 

 

#Loop para solicitar 15 vezes 

for i in range (1,16,1): 

    valor=int(input('Digite um valor:\n')) 

    respostas=valores.append(valor) 

 

#Somar valores da lista 

sum= sum(valores) 

 

#Exibir soma 

print(sum) 