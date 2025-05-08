# 1 - Fatorial de um número

def factorial (num):
    if num == 1:
        return 1
    else:
        return(num*factorial(num -1))

number = int(input('Digite o número para o fatorial:\n'))
print(f'O fatorial de {number} é: {factorial(number)}')

# 2 - soma total de um número
def soma (num):
    if num == 1:
        return 1
    else:
        return(num+soma(num - 1))

numero = int(input('Digite o número para a soma:\n'))
print(f'a soma de {numero} é: {soma(numero)}')