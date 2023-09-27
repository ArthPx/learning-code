matriz = [[0,0,0],[0,0,0],[0,0,0]]
count = 0
countc = 0
maior = 0

for l in range (0,3):
    for c in range (0,3):
        matriz[l][c]= int(input(f'Valor em {[l]}x{[c]}:'))
        if matriz[l][c] % 2 == 0:
            count += matriz[l][c]
        if c == 2:
            countc += matriz[l][c]
        if l == 1:
            if c==0:
                maior = matriz[l][c]
            elif matriz[l][c]>maior:
                maior = matriz[l][c]
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()           
print(f'{matriz[l][c]}')
print(f'Soma de todos os numeros pares: {count}')
print(f'Soma de todos os números da 3ª Coluna: {countc}')
print(f'Maior Número da segunda linha: {maior}')

