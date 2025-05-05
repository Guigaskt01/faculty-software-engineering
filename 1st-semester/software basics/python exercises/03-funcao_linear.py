"""Elaborar um programa para calcular o valor de y como função de x,
segundo a função y(x)=3x+2, em um domínio real."""

#Esperar valor do usuário
valor_x=int(input('Dê um valor ao X\n'))

#Realizar calculo da função
valor_y=( 3 * valor_x ) + 2

#Exibir valor de y
print(f'O valor de Y é \033[32m{valor_y}\033[m')