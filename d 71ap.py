print('=-' *20)
print('Banco Arnaldo')
print('=-' * 20)
ced = 50
totced = 0
saque = int(input('Qual valor a ser sacado?'))
while True:
    if saque >= ced:
        saque -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} Cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if saque == 0:
            print('Volte sempre !!!') 
            break


