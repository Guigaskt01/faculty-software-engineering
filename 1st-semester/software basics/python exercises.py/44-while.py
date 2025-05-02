"""Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida
pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o 
número 1 a repetição termina. Exibir no final todos os elementos da lista."""

numeros_positivos_e_pares=[]

numero=int(input('Digite um número aleatório:\n'))

while numero != 1:
    if numero % 2 == 0 and numero > 0:
        numeros_positivos_e_pares.append(numero)
        
    numero=int(input('Digite um número aleatório:\n'))


print('Encerrando programa...')
print(f'Números pares e positivos obtidos: {numeros_positivos_e_pares}')
        
