pares = 0
count9 = 0
valores = (int(input('Digite um número ')), int(input('Digite mais um número ')), int(input('Digite mais um número ')),
            int(input('Digite o ultimo número ')))
print(f'Valores digitados: {valores}')
if 9 in valores: ### há o metodo count 'valores.count(9)' fiz diferente pra ver como fica, mas o count é bem mais pratico
    count9 += 1
print(f'Há {count9} números 9 na tupla')
if 3 in valores: ### pode usar uma função feita para isso 'valores.index(3)' fiz um metodo para mostrar TODAS AS POSIÇÕES DO 3, ou seja,  quando tem mais de um 3
    for pos,t in enumerate(valores):   
        if t == 3:
            print(f'Existe um 3 na posição {pos+1}')
for c in valores:
    if c % 2 == 0:
        print(f'{c} é Par',end=' ')
