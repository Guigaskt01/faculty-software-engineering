import statistics

#1- Aplicar a média em uma lista de números
print(statistics.mean([1, 2, 3, 4, 5])) # Média aritmética

#2- Aplicar a mediana em uma lista de números
print(statistics.median([1, 2, 3, 4, 5])) # Mediana (retorna valor central da lista)
print(statistics.median([1, 2, 3, 7, 8, 9])) # Mediana (retorna valor central da lista)(quando se tem dois numeros no meio faz a media)

#3- Aplicar a moda em uma lista de números
print(statistics.mode([1, 2, 3, 4, 5, 5])) # Moda (retorna o número que mais se repete na lista)

#4- Aplicar desvio padrao
'''Quanto mais p´roximo de 0 for o desvio padrão, significa que osdados do conjunto estao menos dispersos em relação a média.'''

print(statistics.stdev([1, 2, 3, 4, 5])) # Desvio padrão (quanto mais próximo de 0, menos dispersos os dados estão em relação à média)