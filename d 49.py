n= int(input('Qual o número que você deseja saber sua tabuada?'))
f= int(input('Você quer uma tabuada de até x quantos? '))
m=1
for c in range (0,f+1):
    m= n*c
    print(f'{n} x {c} é igual a {m}')

