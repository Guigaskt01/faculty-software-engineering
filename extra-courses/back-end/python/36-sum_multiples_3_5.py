"""Elaborar um algoritmo que some todos os numeros inteiros abaixo de 1000 
que sao muliplos de 3 e 5""" 

 

numeros = [] 

 

for i in range(1000): 

    if i % 3 == 0 and i % 5 == 0: 

        numeros.append(i) 

 

soma = sum(numeros) 

 

print(f"Soma dos múltiplos de 3 e 5 abaixo de 1000:{soma}") 