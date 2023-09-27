
cont= 0
num = 0
total = 0
print('Digite 999 para parar o programa')
while num != 999:
    num = int(input('Digite um número:'))
    if num!= 999:
        total += num
        cont +=1
print(f'Foram digitados {cont} números e a soma entre eles foi {total} ')
print('Fim!!')
    