game_name= 'Fortnite'
game_description= """
    Fortnite é um jogo battle royale,
    com 100 jogadores ao redor do mapa
    e o ultimo sobrevivente ganha,po-
    dendo utilizar construções para 
    se defender.
"""

# String [:fim] [inicio:] - fatiamento
#Indice começa na posição 0

#1- busque toda string a partir da primeira posição
print(game_name[0:])

#2- Busque toda string ate a ultima posição
print(game_name[:8])

#3- Busque toda string até a terceira posição (posição nao indice)
print(game_name[2:])

#4- Busque toda string de 2 em 2 caracteres
print(game_name[::2])

#5- busque toda string nos indices impares
print(game_name[1::2])

#6- Inverter uma stringe de tras para frente
print(game_name[::-1])