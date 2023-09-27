valores = list()
c = 's'

while True:

    valores.append(int(input('Valor:')))
    c= str(input('Deseja continuar?[s/n]:')).lower().strip()[0]
    if c != 's':
        print( '=-'*30)
        print(f'Foram digitados {len(valores)} valores ')
        valores.sort(reverse= True)
        print(f'Lista de valores decrescente {valores}')
        if 5 in valores:
            print(f'Há {valores.count(5)} numeros 5 na lista')
            break

        else:
            print(f'Não há nenhum número 5 na lista')
            break



        
