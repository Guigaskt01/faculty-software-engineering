n1=int(input('Digite o primeiro número:\n'))
n2=int(input('Digite o segundo número:\n'))

#Aritméticos (3 % 2 = 1) | 4² = 4 * 4

sum=n1+n2
sub=n1-n2
div=n1/n2
mul=n1*n2
mod=n1%n2
exp=n1**n2

print(f"Resto da divisão de {n1} por {n2} é {mod}")
print(f"Potência do número {n1} por {n2} é {exp}")

#Comparação (se nao coincidir com o resultado, ao exibir no print ele será false)
bigger = n1 > n2
smaller = n1 < n2
equal = n1 == n2
different= n1 != n2
bigger_equal= n1 >= n2
smaller_equal= n1 >= n2

print(f"Os números {n1} e {n2} são iguais? {equal}")
print(f"O número {n1} é maior ou igual a {n2}? {bigger_equal}")

#Atribuição
# podemos utilizar quando queremos concatenar um operador com outro
n1 += 1 # n1 = n1+1
n1 -= 1 # n1 = n1-1
n1 *= 1 # n1 = n1*1
n1 /= 1 # n1 = n1/1