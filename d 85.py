num = [[],[]]
p = 's'
for i in range(0,6):
    no = int(input('Valor:'))
    if no % 2 == 0:
        num[0].append(no)
    else:
        num[1].append(no)
print(f'Todos os valores {sorted(num)}')
print(f'Numeros pares {sorted(num[0])}')
print(f'Numeros ímpares {sorted(num[1])}')
