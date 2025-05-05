"""11) Elaborar um programa que calcule a aceleração de um corpo em movimento
conhecendo-se as velocidades inicial e final, e o intervalo de tempo medido
(a = (v2 –v1)/Δt). Exibir o resultado."""

# Esperar valores do usuário
velocidade_inicial= float(input('Digite a velocidade inicial (em metros por segundo):\n'))

velocidade_final= float(input('Digite a velocidade final (em metros por segundo):\n'))

tempo_medido= float(input('Digite o intervalo de tempo (em segundos):\n'))

# Calcular a aceleração
aceleracao = (velocidade_final - velocidade_inicial) / tempo_medido

# Exibir o resultado
print(f'A aceleração do corpo é {aceleracao:.2f} metros por segundo ao quadrado.')