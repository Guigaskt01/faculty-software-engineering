"""5) Elaborar um algoritmo que solicita ao usuário para digitar 15 valores
e deve exibir a soma e média. """

# Criar lista para armazenar os valores
valores = []

# Loop para solicitar 15 valores
for i in range(1, 16):
    valor = int(input(f'Digite o {i}º valor:\n'))
    valores.append(valor)  # Adiciona o valor na lista

# Soma de todos os valores da lista
soma = sum(valores)

# Cálculo da média
media = soma / len(valores)

# Exibir soma e média
print(f'A soma dos valores é: {soma}')
print(f'A média dos valores é: {media:.2f}')