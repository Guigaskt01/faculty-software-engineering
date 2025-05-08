gameFifa={
    'name':'Fifa 23',
    'yearLaunch': 2022,
    'gamePrice':90.50,
    'classification':8.5,
    'genre': ['esporte','família']
}

print (gameFifa)
print (len(gameFifa))
print (type(gameFifa))

#1- Recuperar oum elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

#2- Buscar apenas as chaves do dicionário
print(gameFifa.keys())

#3- Buscar apenas os valores do dicionário
print(gameFifa.values())

#4- Buscar itens do dicionário com chave e valor
print(gameFifa.items())

#5- Adicionar itens ao dicionário
gameFifa['players']=2
print(gameFifa)

#6- Atualizar itens no dicionário
gameFifa.update({'players':1})
print(gameFifa)

#7- Remover item no dicionário
gameFifa.pop('players')
print(gameFifa)