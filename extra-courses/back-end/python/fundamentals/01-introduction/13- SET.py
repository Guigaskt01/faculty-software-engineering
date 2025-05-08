games_set={'Fifa23', 'Red Dead 2', 'Star Wars',
                'Mario Odyssey','The Legend of Zelda'}

#Não possibilita recuperar valores via fatiamento ou slice

#1- Buscar o tamanho do set
print(len(games_set))

#2- True e 1 sao considerados o mesmo valor
example_Set={'FIFA 23', True,1,90.50}
print(example_Set)

#3- Adicionar item de outro set
games_set.update(example_Set)
print(games_set)

#4- Remover um item no set
games_set.remove(True)
games_set.remove(90.50)
print(games_set)