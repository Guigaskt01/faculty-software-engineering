games_tuple=('Fifa23', 'Red Dead 2', 'Star Wars',
                'Mario Odyssey','The Legend of Zelda' )

print(games_tuple)
print(type(games_tuple))

#TUPLA
#Não possibilita adicionar valores na tupla
#Não possibilita remover valores na tupla
#Não possibilita ordenar valores na tupla

#1- Buscar os dois primeiros itens da tupla
print(games_tuple[0:2])

#2- Buscar o ultimo item da lista
print(games_tuple[-1])

#3- Buscar jogos até uma determinada posição
print(games_tuple[:3])

#4- Buscar jogos de uma posição em diante
print(games_tuple[2:])

#5- Recuperar um item da tupla pelo índice
print(games_tuple.index('Fifa23'))
