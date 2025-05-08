# 1 - Crie uma função que receba dois argumentos: O primeiro nome e o segundo nome
def full_name(fname, lname):
    print(f'Nome Completo: {fname} {lname}')

full_name('guilherme','rodrigues')

# 2 - Crie uma função que some dois números via parâmetros
def sum(a, b):
    return a + b

print(sum(10,50))

# 3 - Argumentos default numa função
def address(country='Brazil'):
    print(f'Eu moro no {country}')

address()
address('Canadá')

# 4 - Avaliação de jogo
def rating_game(qtd_rating):
    game_name=input('Digite o nome do jogo \n')
    sum=0
    for i in range(qtd_rating):
        note=float(input('Digite a nota para o jogo \n'))
        sum += note # sum = sum + note
    print(f'Média de avaliação do jogo {game_name} é: {sum/qtd_rating}')

rating_game(2)

# OU

def rating_game(qtd_rating):
    game_name=input('Digite o nome do jogo \n')
    sum=0
    for i in range(qtd_rating):
        note=float(input('Digite a nota para o jogo \n'))
        sum += note # sum = sum + note
    print(f'Média de avaliação do jogo {game_name} é: {sum/qtd_rating}')

rating=(int(input('Digite quantas avaliações deseja fazer no jogo \n')))
rating_game(rating)
rating_game(rating)
rating_game(rating)