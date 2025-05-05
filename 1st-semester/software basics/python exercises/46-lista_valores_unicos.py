"""Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida
pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista"""

# Inicializa uma lista vazia para armazenar os valores
valores = []

# Inicializa um conjunto para rastrear os valores já adicionados
ja_adicionados = set()

# Solicita ao usuário que digite 15 valores reais
print('Digite 15 valores reais (sem repetição).')

# Loop para preencher a lista com valores únicos
while len(valores) < 15:
    numero = int(input(f'Valor {len(valores)+1}: '))
    if numero in ja_adicionados:
        print('Valor já adicionado, tente novamente.')
    else:
        # Adiciona o número à lista se não for repetido
        valores.append(numero)
        # Adiciona o número ao conjunto para rastrear os já adicionados
        ja_adicionados.add(numero)
        
# Exibe a lista final com os valores únicos
print('Lista final:', valores)