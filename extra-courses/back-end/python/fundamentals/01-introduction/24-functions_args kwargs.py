"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

# 1 - Soma de números (args)
def sum(*num):
    sum_total=0
    for n in num:
        sum_total += n 
    print(f'Soma é {sum_total}')

sum(7)
sum(7,3)
sum(13,7)


# 2 - Apresentação de cursos (kwargs)
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

print('####Curso####')
presentation(name='Python', category='Backend',level='Iniciante')