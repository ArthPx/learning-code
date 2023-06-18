a= int(input('Primeiro numero'))
b = int(input('Segundo numero'))
c = int(input('Terceiro numero'))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
print('O menor é \033[1;36m{}\033[m'.format(menor))
maior=a
if b>a and b>c:
    maior= b
if c>a and c>b:
    maior= c
print('O maior é \033[36m{}\033[m'.format(maior))





