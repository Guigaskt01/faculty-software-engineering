gamelist=['Fortnite','Valorant','R.E.P.O','Ark Survival',
            'COD', 'roblox']

#1- Tamanho da lista
print(len(gamelist)) #LEN retorna a quantidade de itens dentro da lista

#2- Recuperar um item da lista pelo índice
print(gamelist.index('R.E.P.O')) #INDEX retorna índice do item que deseja  dentro da lista | Muito bom para grandes listas 

#3- Adicionar item ao final da lista
gamelist.append('pokemon gba') #APPEND adiciona item dentro da lista
print(gamelist)
print(len(gamelist)) # retorna quantidade de items dentro da lista/ interessante observar que antes era 6, após o append foi para 7

#4- Ordenar a lista
gamelist.sort()
print(gamelist)

#5- Copiar uma lista de jogos para outra
gamereset=gamelist.copy()
gamereset.remove()=input()
print(gamereset)

#6- Remove todos os itens da lista
gamelist.clear()
print(gamelist)