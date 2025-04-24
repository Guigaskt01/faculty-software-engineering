'''Elaborar um programa que leia o tempo de duração de um evento em uma 
fábrica expressa em segundos e mostre-o expresso em horas,minutos e segundos.'''

horas=int(input('Informe o número de horas\n'))
minutos=int(input('Informe o número de minutos\n'))
segundos=int(input('Informe o número de segundos:\n'))

#calculo do tempo total em segundos
tempo_total_segundos=(horas*3600)+(minutos*60)+segundos