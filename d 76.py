print(f'{"Tabela da casa do seu jao":^30}')
tabela = ('estojo',12.99,'lapis',8.99,
          'caneta',5.55,'tesoura',2.59,
          'caderno',22.99,'mochila',100)
for c in range(0,len(tabela)):
    if c %2 == 0 or c == 0:
        print(f'{tabela[c]:<30}', end='')
    else:
        print(f'R${tabela[c]:>.2f}\n')
