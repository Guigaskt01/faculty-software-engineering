"""6) Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros.
 No final, o programa deve exibir quantos números são múltiplos de 3,
  quantos números são menores que 45 e maiores que 55, e qual é o menor número entre eles. """

 

todos_valores = []
multiplos_3 = []
menores_45 = []
maiores_55 = []

# Loop para solicitar valor 10 vezes
for i in range(1, 11):
    num = int(input('Digite um valor:\n'))
    todos_valores.append(num)

    # Verifica se número é múltiplo de 3
    if num % 3 == 0:
        multiplos_3.append(num)

    # Verifica se número é menor que 45 ou maior que 55
    if num < 45:
        menores_45.append(num)
    elif num > 55:
        maiores_55.append(num)

# Exibe os resultados
print(f'\nQuantidade de números múltiplos de 3: {len(multiplos_3)}')
print(f'Quantidade de números menores que 45: {len(menores_45)}')
print(f'Quantidade de números maiores que 55: {len(maiores_55)}')
print(f'O menor número digitado foi: {min(todos_valores)}')