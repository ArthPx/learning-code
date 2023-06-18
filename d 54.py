
from datetime import date
menor = 0
maior = 0
atual = date.today().year
for c in range (1,8):
    nasc = int(input(f'Em qual ano a {c}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
     maior += 1
    elif idade < 18:
        menor += 1
print(f'Tem ao total {maior} maiores de idade e {menor} menores de idade')

