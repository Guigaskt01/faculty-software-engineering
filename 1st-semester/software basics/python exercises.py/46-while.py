"""10) Elaborar um programa que contem uma lista com 15 elementos. Essa lista deve ser preenchida
pelo usuário, porém não deve conter valores repetidos. Exibir no final a lista"""

valores = []
ja_adicionados = set()  # Conjunto para rastrear valores já adicionados
print('Digite 15 valores reais (sem repetição).')

while len(valores) < 15:
    numero = int(input(f'Valor {len(valores)+1}: '))
    if numero in ja_adicionados:
        print('Valor já adicionado, tente novamente.')
    else:
        valores.append(numero)
        ja_adicionados.add(numero)  # Adiciona o número ao conjunto de já adicionados
        
# Exibe a lista final com os valores únicos
print('Lista final:', valores)