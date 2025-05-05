"""4) Um produto vai sofrer aumento de acordo com a tabela abaixo. Elaborar um programa que leia 
o preço antigo, calcule e mostre o preço novo, e mostre uma mensagem em função do preço 
novo (de acordo com a segunda tabela)
_________________________________________________         __________________________________________________
|preço antigo         |   percentual de aumento |         |preço novo                        | mensagem    |
|Até R$50             |           5%            |         |até R$ 80                         | Barato      |
|Entre R$ 50 e R$ 100 |          10%            |         |entre R$ 80 e R$ 120 (inclusive)  | normal      |
|Acima de R$100       |          15%            |         |entre R$ 120 e R$ 200 (inclusive) | caro        |
-------------------------------------------------         |acima de R$ 200                   | muito caro  |
"""

#Solicita o preço antigo do produto
preco_antigo=float(input('Digite o valor antigo do produto:\n'))

#Verifica percentual de aumento de acordo com preço antigo
if preco_antigo <= 50:
    preco_novo=(preco_antigo*1.05) 

elif preco_antigo <= 100:
    preco_novo=(preco_antigo*1.10)

else:
    preco_novo=(preco_antigo*1.15)

#Exibe mensagem preço novo e verifica se está caro ou não
if preco_novo <= 80:
    print('Barato')

elif preco_novo  <= 120:
    print('Normal')

elif preco_novo < 120 and preco_novo <= 200:
    print('Caro')

else:
    print('Muito caro')

#Exibe valor antigo e preço novo para notar a diferença depois do aumento
print(f"O valor antigo era R${preco_antigo:.2f}, o novo valor é R${preco_novo:.2f}")