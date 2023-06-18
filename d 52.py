num = int(input('Digite um número inteiro:. '))
contador = 0
for c in range (1,num +1):
    if num%c == 0:
         contador = contador + 1
if contador >= 3:
    print(f'{num} não é um número primo!')
else:
    print(f'{num} É um número primo !')
