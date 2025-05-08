import re


text='OneBitCode: Transformamos pessoas em programadores.'

#1- indice inicial e final de palavras
#O  r significa que a string é uma raw string, ou seja, não tem escape de caracteres
match=re.search(r'pessoas em programadores', text) #retorna o primeiro match encontrado
print(match.start()) #retorna o índice inicial da palavra
print(match.end()) #retorna o índice final da palavra

#2- Buscando o índice que possui o ponto no meu site
site='www.onebitcode.com'
match=re.search(r'\.', site) #retorna o primeiro match encontrado
print(match) #retorna o índice inicial da palavra

#3- Buscando uma lista de caracteres dentro de uma frase

padrao='[a-m]'
resultado=re.findall(padrao, text) #retorna uma lista com os caracteres que estão dentro do padrão
print(text) #retorna a string original
print(resultado) #retorna uma lista com os caracteres que estão dentro do padrão

#4- verificando o inicio de uma string
rule=r'^A'
frase=['A casa está suja', 'O dia está lindo', 'Vamos passear']
for i in frase:
    match=re.search(rule, i) #retorna o primeiro match encontrado
    if match:
        print(f'A frase "{i}" começa com a letra "A"')
    else:
        print(f'A frase "{i}" não começa com a letra "A"')

#5 - verificando o final de uma string
rule_end=r'!$'
frase2='O dia está lindo!'
match=re.search(rule_end, frase2) #retorna o primeiro match encontrado
if match:
    print(f'A frase "{frase2}" termina com "!"')
else:
    print(f'A frase "{frase2}" não termina com "!"')