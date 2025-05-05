"""Elaborar um programa para automatizar o caixa de uma lanchonete.
Este programa deve ler o código do item pedido, a quantidade e 
somar para calcular o valor a ser pago. O programa termina quando o código for 0 (zero).
O cardápio da lanchonete é o seguinte:"""

# Definindo os códigos dos itens, nomes e seus respectivos valores
codigo = [100, 101, 102, 103, 104, 105, 0]

# Nomes dos itens do cardápio
item = ['Cachorro Quente', 'Bauru Simples', 'Bauru c/ovo',
        'Hamburguer', 'Cheeseburguer', 'Refrigerante', 'Sair']

# Preços dos itens do cardápio
valor = [3.50, 3.80, 4.50, 4.70, 5.30, 4.00, 0.00]

# Inicializando a variável de total do pedido
total = 0

# Pergunta se o cliente deseja começar um novo pedido
novo_pedido = input('Deseja começar um novo pedido? (S/N)\n').upper()

# Enquanto o usuário digitar 'S' (sim), o loop continuará
while novo_pedido == 'S':
    print('\nMENU')

    # Exibe os itens do menu com os códigos, nomes e preços
    for i in range(len(codigo)):
        print(f'{codigo[i]} - {item[i]} - R$ {valor[i]:.2f}')

    # Pergunta o código do item que o cliente deseja
    escolha_pedido = int(input('Digite o código do item desejado:\n'))

    # Se o código for 0, encerra o pedido
    if escolha_pedido == 0:
        print('Encerrando pedido...')
        novo_pedido = 'N'

    # Se o código for válido (existe no menu), prossegue com a escolha
    elif escolha_pedido in codigo:

        # Encontra o índice do código selecionado
        indice = codigo.index(escolha_pedido)
        
        # Exibe o item selecionado e seu preço
        print(f'Item selecionado: {item[indice]} - R$ {valor[indice]:.2f}')

        # Pergunta a quantidade do item desejado
        quantidade = int(input(f'Quantos {item[indice]} você deseja? '))

        # Calcula o subtotal para este item
        subtotal = valor[indice] * quantidade

        # Atualiza o total com o valor do subtotal
        total += subtotal

        # Exibe o subtotal do item
        print(f'Subtotal do item: R$ {subtotal:.2f}')

        # Pergunta se o cliente deseja continuar comprando
        novo_pedido = input('Deseja pedir mais alguma coisa? (S/N)\n').upper()

    else:

        # Se o código digitado não for válido, avisa o cliente
        print('Código inválido. Tente novamente.')

# Exibe o valor total da compra ao final
print(f'\nValor total de sua compra foi de R$ {total:.2f}')