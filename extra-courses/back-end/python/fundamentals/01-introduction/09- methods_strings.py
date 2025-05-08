game_name= 'Fortnite'
game_description= """
    Fortnite é um jogo battle royale,
    com 100 jogadores ao redor do mapa
    e o ultimo sobrevivente ganha,po-
    dendo utilizar construções para 
    se defender.
"""

print(game_name.upper()) # Retorna string em maiúsculo
print(game_name.lower()) # Retorna string em minusculo
print(game_name.capitalize()) #Apenas primeira letra em maiusculo
print(game_name.title()) #Apenas primeira letra em maiusculo
print(game_name.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(game_name.find('F')) #Retorna a posição de um determinado caractere
print(game_description.count('e')) #Conta caracteres
print(game_description.count('a')) #Conta caracteres
print(game_description.replace("Fortnite", "COD")) #Altera um elemento por outro
print(game_description.split(','))