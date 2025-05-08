#1 - Função para imprimir Hello World
def wellcome():
    print('Hello World')

wellcome()

# 2 - Função para somar dois números
def sum():
    return 5+4

sum()

# 3 - Função para cadastrar um jogo
def create_game():
    name=input('Digite o nome do jogo\n')
    year_launch=int(input('Digite o ano de lançamento do jogo\n'))
    game_price=float(input('Digite o preço do jogo\n'))
    note_rating=input('Digite a nota de avaliação do jogo:\n')

    print(f'{name} - R$ {game_price:.2f}')

create_game()
create_game()


