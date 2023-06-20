num= int(input('Digite um número para ver seu fatorial:'))
cont = num
som=1
while cont>0:
    som *= cont
    cont-=1
print(f'O fatorial de {num} é {som}')
''' fatorial'''