dados = []
todos = []
mai = 0
men = 0
p = 's'
while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    if len(todos) == 0:
        mai=men= dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < mai:
            men = dados[1]
    p = str(input('Deseja continuar?[s/n]:')).lower().strip()[0]
    todos.append(dados[:])  
    dados.clear() 
    if p != 's':
        break

print(f'Foram cadastradas {len(todos)} Pessoas')
print('=-'*30)
print(f'Lista dos mais pesados')
for i in todos:
    if i[1] == mai:
        print(f'{i[0]}')
print('=-' * 30)
print(f'Lista dos mais leves')
for e in todos:
    if e[1] == men:
        print(f'{e[0]}')
