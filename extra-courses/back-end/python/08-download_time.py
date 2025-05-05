import time
"""Elaborar um programa que dados o tamanho de um arquivo (em bits),
bem como a velocidade da conexão (em bits por segundo),
informe o tempo necessário para o download do arquivo."""

# Esperar valores do usuário
tamanho_arquivo = float(input('Digite o tamanho do arquivo (em bits):\n'))
vel_conexao = float(input('Digite a velocidade de conexão (em bits por segundo):\n'))

# Descobrir o tempo de download em segundos
tempo_download_segundos = tamanho_arquivo / vel_conexao

# Converter para minutos
tempo_download_minutos = tempo_download_segundos / 60

# Exibir tempo de download em segundos e minutos
print(f'O tempo necessário para download é {tempo_download_segundos:.2f} segundos ({tempo_download_minutos:.2f} minutos).')