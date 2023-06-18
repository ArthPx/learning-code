maior = 0 
menor = 0
for c in range (1, 6):
    peso = float(input(f'Qual é o peso da {c}º pessoa? '))
    if c == 1:
        maior = peso
        menor = peso
    else: 
        if  peso > maior:
            maior = peso
        if  peso < menor:
            menor = peso
print(f'O menor PESO é {menor} e o maior PESO é {maior}')
