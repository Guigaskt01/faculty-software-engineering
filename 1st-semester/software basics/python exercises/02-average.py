"""Elaborar um programa que receba quatro números inteiros,
 que calcule e mostre a soma e a média desses números."""

#Esperar valores pelo usuário
n1=int(input('Digite um número\n:'))
n2=int(input('Digite um número\n:'))
n3=int(input('Digite um número\n:'))
n4=int(input('Digite um número\n:'))

#Somar numeros inteiro
soma=n1+n2+n3+n4 

#Encontrar a média da soma
media=soma/4

#Exibir total da soma e a média da soma
print(f'a soma dos valores atribuidos é {soma} e a média é {media:.2f}') 