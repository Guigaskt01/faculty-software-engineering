"""1) Elaborar um algoritmo que leia um valor de temperatura em graus Celsius, 
calcule e exiba a temperatura equivalente em Kelvin, sabendo que: K = C + 273. 
Esse algoritmo deve repetir 5 vezes. """

 

 

#Loop para solicitar 5 vezes 

for c in range(1,6,1): 

    celsius=int(input('Informe a temperatura atual em graus Celsius:\n')) 

    kelvin=celsius + 273 

 

    print(f'atualmente o valor de celsius é {celsius}, convertido para Kelvin ele é {kelvin}') 