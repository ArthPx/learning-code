geral = list()
pares = list()
impares = list()
p = 's'
while True:
    geral.append(int(input('Valor:')))
    p = str(input('Quer continuar?[s/n]')).lower()[0]
    if p != 's':
        break
for c in geral:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print('=-'*30)
print(f'Lista com todos os elementos:\n{geral}')
print(f'Lista com todos os elementos pares:\n{pares}')
print(f'Lista com todos os elementos ímpares:\n{impares}')
