#1- Liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i <4 :
#         print(i)

list_numbers=[i for i in range(10) if i <4]
print(list_numbers)

game_list= ["Mario Odyssey", "Donkey Kong Country",
            "Luigi's mansion", "Kirby"]

#2- Jogos que possuam a letra 'a'
new_list=[x for x in game_list if 'a' in x]
print(new_list)

#3- jogos que eu zerei
games_finished=[x for x in game_list if x != 'Kirby']
print(games_finished)