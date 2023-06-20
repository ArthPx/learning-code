total=0
for c in range (1,7):
    num= int(input('Digite um número inteiro'))
    if num %2 != 0:
        total += num
    else:
        print('Esse numero não é ímpar')
print(f'A soma de todos os numeros impares digitados é {total}')

    