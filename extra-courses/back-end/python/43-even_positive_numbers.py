"""Elaborar um programa que contem uma lista com N elementos. Essa lista deve ser preenchida
pelo usuário e só deve conter números inteiros positivos e pares. Caso o usuário digite o 
número 1 a repetição termina. Exibir no final todos os elementos da lista."""

# Inicializa uma lista vazia para armazenar os números positivos e pares
numeros_positivos_e_pares = []

# Solicita o primeiro número ao usuário
numero = int(input('Digite um número aleatório:\n'))

# Enquanto o número digitado for diferente de 1, o loop continuará
while numero != 1:
    # Verifica se o número é par e positivo
    if numero % 2 == 0 and numero > 0:
        # Se for par e positivo, adiciona à lista
        numeros_positivos_e_pares.append(numero)
    
    # Solicita ao usuário um novo número
    numero = int(input('Digite um número aleatório:\n'))

# Quando o número 1 é digitado, encerra o programa
print('Encerrando programa...')

# Exibe a lista com todos os números pares e positivos inseridos
print(f'Números pares e positivos obtidos: {numeros_positivos_e_pares}')

        
