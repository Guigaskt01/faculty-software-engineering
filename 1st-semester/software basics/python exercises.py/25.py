"""5) Elaborar um programa para automatizar o caixa de uma lanchonete. Este algoritmo deve ler o 
código do item pedido, a quantidade e calcular o valor a ser pago por aquele lanche. No final o 
programa deve mostrar o total a ser pago. O cardápio da lanchonete é o seguinte
_____________________________________________________
| Código   | Especificação     | Preço Unitário (R$) |
|   100    | Cachorro quente   |     3,50            |
|   101    | Bauru simples     |     3,80            |
|   102    | Bauru c/ovo       |     4,50            |
|   103    | Hamburguer        |     4,70            |
|   104    | Cheeseburger      |     5,30            |
|   105    | Refrigerante      |     4,00            |
------------------------------------------------------
"""
#Solicita o codigo do pedido
codigo = int(input('Por favor, escreva o código do pedido que o senhor deseja:\n'))

#Verifica o codigo do pedido
if codigo == 100:
    cachorro_quente = 3.50
    quantidade = int(input('Selecionado Cachorro Quente. Quantos você deseja?\n'))
    total_pagar = cachorro_quente * quantidade
    print(f'Ótima escolha! Foram {quantidade} cachorro(s) quente(s). Total a pagar: R$ {total_pagar:.2f}')

elif codigo == 101:
    bauru_simples = 3.80
    quantidade = int(input('Selecionado Bauru Simples. Quantos você deseja?\n'))
    total_pagar = bauru_simples * quantidade

    #Exibe quantidade e valor total a pagar
    print(f'Ótima escolha! Foram {quantidade} bauru(s) simples. Total a pagar: R$ {total_pagar:.2f}')

elif codigo == 102:
    bauru_com_ovo = 4.50
    quantidade = int(input('Selecionado Bauru com Ovo. Quantos você deseja?\n'))
    total_pagar = bauru_com_ovo * quantidade

    #Exibe quantidade e valor total a pagar
    print(f'Ótima escolha! Foram {quantidade} bauru(s) com ovo. Total a pagar: R$ {total_pagar:.2f}')

elif codigo == 103:
    hamburguer = 4.70
    quantidade = int(input('Selecionado Hambúrguer. Quantos você deseja?\n'))
    total_pagar = hamburguer * quantidade

    #Exibe quantidade e valor total a pagar
    print(f'Ótima escolha! Foram {quantidade} hambúrguer(es). Total a pagar: R$ {total_pagar:.2f}')

elif codigo == 104:
    cheeseburguer = 5.30
    quantidade = int(input('Selecionado Cheeseburguer. Quantos você deseja?\n'))
    total_pagar = cheeseburguer * quantidade

    #Exibe quantidade e valor total a pagar
    print(f'Ótima escolha! Foram {quantidade} cheeseburguer(es). Total a pagar: R$ {total_pagar:.2f}')

elif codigo == 105:
    refrigerante = 4.00
    quantidade = int(input('Selecionado Refrigerante. Quantos você deseja?\n'))
    total_pagar = refrigerante * quantidade

    #Exibe quantidade e valor total a pagar
    print(f'Ótima escolha! Foram {quantidade} refrigerante(s). Total a pagar: R$ {total_pagar:.2f}')

#Codigo não existente exibe mensagem como "Inválido"
else:
    print('Código inválido. Por favor, escolha um código entre 100 e 105.')