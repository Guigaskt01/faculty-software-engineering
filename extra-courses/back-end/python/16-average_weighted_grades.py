"""16) Elaborar um programa que leia 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente."""

# Esperar os valores das notas do aluno
nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))
nota3 = float(input('Digite a terceira nota:\n'))

peso1 = 2
peso2 = 3
peso3 = 5

# Calcular a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Exibir a média ponderada
print(f'A média ponderada do aluno é {media_ponderada:.2f}')