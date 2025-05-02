"""Elaborar um programa para automatizar o caixa de uma lanchonete.
Este programa deve ler o código do item pedido, a quantidade e 
somar para calcular o valor a ser pago. O programa termina quando o código for 0 (zero).
O cardápio da lanchonete é o seguinte:"""

codigo=[100,101,102,103,104,105,0]

item=['Cachorro Quente', 'Bauru Simples', 'Bauru c/ovo',\
       'Hamburguer', 'Cheeseburguer','Refrigerante','Sair']

valor=[3.50,3.80,4.50,4.70,5.30,4.00,0.00]

total=0

novo_pedido=input('Deseja começar um novo pedido?(S/N)\n').upper()

while novo_pedido == 'S':

    print('\nMENU')

    for i in range(len(codigo)):
        print(f'{codigo[i]} - {item[i]} - R$ {valor[i]:.2f}') 

    escolha_pedido=int(input('Digite o código que deseja:\n'))

    if escolha_pedido == 0:
        print('Encerrando Pedido...')
        novo_pedido='N'
    else:
        for i in range(len(codigo)):
            if escolha_pedido == codigo[i]:
                print(f'Item selecionado: {item[i]}, R$ {valor[i]:.2f}')
                quantidade=int(input(f'Quantos {item[i]} você deseja?'))
                subtotal=valor[i]*quantidade
                total += subtotal
                print(f'O valor total do seu pedido foi de R$ {subtotal:.2f}')

print(f'Valor total de sua compra foi de R$ {total:.2f}')

    
    

    


           

