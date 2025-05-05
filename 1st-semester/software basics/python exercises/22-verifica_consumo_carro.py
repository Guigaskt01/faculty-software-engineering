"""2) Elaborar um programa que leia a distancia em km e a quantidade de litros de gasolina 
consumidos por um carro em um percurso, calcule o consumo em Km/l e mostre uma mensagem 
de acordo com a tabela abaixo:"""

"""
-------------------------------------
| CONSUMO  |  KM   | MENSAGEM       |
|-----------------------------------|
|menor que| 8     | venda o carro!  |
|entre    |8 e 14 | Econômico!      |
|maior que|  14   | Super Econômico!|
-------------------------------------
"""

#Solicita Distancia percorrida.
distancia_km=float(input('Digite qual foi a distãncia que o carro percorreu:\n'))

#Solicita quantidade de gasolina em litros.
quantidade_de_litros=float(input('Digite quantos litros de gasolina foi consumido:\n'))

#Obter consumo por KM/L.
consumo_km=distancia_km/quantidade_de_litros

#verifica se o carro é Econômico ou não.
if consumo_km < 8:
    print('Venda o carro!')
elif consumo_km <= 14:
    print('Econômico!')
else:
    print('Super Econômico!')