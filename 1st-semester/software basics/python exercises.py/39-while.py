"""Elaborar um programa que deve ler N números. Caso o usuário digite zero (0), o programa 
deve exibir a somatória e a média dos valores inseridos"""


armazenarNumeros=[]
numero=float(input('Digite um número:\n'))

while numero > 0:
        armazenarNumeros.append(numero) 

        numero=float(input('Digite um número:\n'))

somar=sum(armazenarNumeros)
media=somar/len(armazenarNumeros)

print(f'Soma: {somar}')
print(f'Media: {media}')