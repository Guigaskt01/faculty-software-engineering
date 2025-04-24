import time
#8) Elaborar um programa que dados o tamanho de um arquivo (em bits), bem como a velocidade da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo.

#Esperar valores do usuário
tamanho_arquivo=float(input('Digite o tamanho do arquivo(em bits):\n'))
vel_conexao=float(input('Digite a velocidade de conexão (em bits por segundo):\n'))

#Descobrir o tempo de download em segundos
tempo_download_segundos= tamanho_arquivo/vel_conexao

#converter o tempo de download para minutos para facilitar entendimento
tempo_download_minutos= tamanho_arquivo/vel_conexao

#exibir tempo de download em minutos
print(f'O tempo necessário para download é {tempo_download_minutos:.2f} segundos ')