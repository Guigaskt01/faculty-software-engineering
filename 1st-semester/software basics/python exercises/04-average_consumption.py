"""Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l),
dado que são conhecidos a distância total percorrida e o volume de combustivel para percorrê-la
(medido em litros)"""

#Esperar valores do usuário
distancia=float(input('Qual foi a distância percorrida?(Quilometros)\n'))
combustivel=float(input('Qual foi o volume de combustivel consumido?(litros)\n'))

#Encontrar a media de combustivel gasto por KM     
media_km=distancia/combustivel

#Exibir media de combustivel gasto por KM
print(f'o consumo médio dessa viagem foi {media_km:.2f}\n')