'''Elaborar um programa que leia o tempo de duração de um evento em uma 
fábrica expressa em segundos e mostre-o expresso em horas,minutos e segundos.'''

# Entrada do tempo total em segundos
tempo_total_segundos = int(input("Digite o tempo de duração do evento (em segundos):\n"))

# Cálculo das horas, minutos e segundos
horas = tempo_total_segundos // 3600
minutos = (tempo_total_segundos % 3600) // 60
segundos = tempo_total_segundos % 60

# Exibir resultado
print(f'O tempo total é {horas} horas, {minutos} minutos e {segundos} segundos.')