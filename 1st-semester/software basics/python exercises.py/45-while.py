"""Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve 
preencher com valores reais. Logo em seguida, deve ser solicitado ao usuário que digite dois 
números. Esses números devem corresponder a posições na lista (caso contrário solicite um 
novo valor). Após inserir os dois números o programa deve exibir a soma dos elementos das 
duas posições da lista."""

valores = []

print('Digite 25 valores reais.')

while len(valores) < 25:
    numero = float(input(f'Valor {len(valores)+1}: '))
    valores.append(numero)

# Solicita a primeira posição (1 a 25) e converte para índice (0 a 24)
posicao01 = int(input('Digite uma posição (1 até 25): '))
while posicao01 < 1 or posicao01 > 25:
    print('Posição inválida, tente novamente')
    posicao01 = int(input('Digite uma posição (1 até 25): '))

# Solicita a segunda posição (1 a 25) e converte para índice (0 a 24)
posicao02 = int(input('Digite outra posição (1 até 25): '))
while posicao02 < 1 or posicao02 > 25:
    print('Posição inválida, tente novamente')
    posicao02 = int(input('Digite outra posição (1 até 25): '))

# Converte para índices de lista (subtrai 1)
indice01 = posicao01 - 1
indice02 = posicao02 - 1

soma_posicao = valores[indice01] + valores[indice02]

print(f"Soma dos elementos nas posições {posicao01} e {posicao02}: {soma_posicao:.2f}")