c50=0
c20 = 0
c10 = 0
c1 = 0
print('Banco dos Crias')
saque = int(input('Valor a ser sacado:'))
while saque !=0:
    if saque - 50 >= 0:
        c50 += 1
        saque = saque -50
    else:
        break
while saque !=0:
    if saque - 20 >= 0:
        c20 += 1
        saque = saque -20
    else:
        break
while saque !=0:
    if saque - 10 >= 0:
        c10 += 1
        saque = saque -10
    else:
        break    
while saque !=0:
    if saque - 1 >= 0:
        c1 += 1
        saque = saque -1
    else:
        break
print(f'{c50} Cedulas(a) de 50R$')
print(f'{c20} Cedulas(a) de 20R$')
print(f'{c10} Cedulas(a) de 10R$')
print(f'{c1} Cedulas(a) de 1R$')
###if saque % 20 >= 0:
    ##print(f'{} Cedulas de 20R$')

    
