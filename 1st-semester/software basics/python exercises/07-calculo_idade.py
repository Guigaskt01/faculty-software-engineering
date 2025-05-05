"""7) Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) idade desta pessoa hoje;
b)A idade desta pessoa em 2035."""

#Esperar valores do usuário
nascimento=int(input('em que ano você nasceu?\n'))
ano_atual=int(input('Digite o ano em que estamos\n'))

#Encontrar sua idade
idade=ano_atual-nascimento

#Descobrir sua idade em 2035
idade_2035=2035-nascimento

#Exibir sua idade e quantos anos terá em 2035
print(f'De acordo com o ano em que você nasceu, você tem {idade} anos, e em 2035 terá {idade_2035} anos.')


