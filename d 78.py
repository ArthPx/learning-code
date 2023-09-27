valores = list()
for c in range (0,5):
    valores.append(int(input(f'Valor para a posição {c}:')))
print('Lista')
print(f'{valores}')
for p,v in enumerate(valores):
    if v == max(valores):
        print(f'O Maior valor da lista É {max(valores)} e está na posição {p}')
    if v == min(valores):
        print(f'O Menor valor da lista É {min(valores)} e está na posição {p}')
    

