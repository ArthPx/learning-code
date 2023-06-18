numero= int(input('Digite um numero de 0 até 9999 '))
print('-'*20)
U = numero//1 % 10
D= numero//10 % 10
C= numero //100 % 10
M= numero // 1000 % 10

print('O seu numero é {}\n Unidade {}\n Dezena {}\n Centena {}\n Milhar {} '.format(numero,U,D,C,M))
print('-'*20)