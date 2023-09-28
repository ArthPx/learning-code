dados = []
todos = []
p = 's'
p1 = 's'
per = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('1ª Nota:')))
    dados.append(float(input('2ª Nota:')))
    dados.append((dados[1] + dados[2]) /2 )
    todos.append(dados[:])
    
    dados.clear()
    p = str(input('Deseja continuar?[S/N]')).lower().strip()[0]
    if p != 's':
        break
txt = 'BOLETIM'
print(txt.center(30,'='))
print(f'{"No.":<4}{"Nome":>8}{"Media":>8}' )
for v,c in enumerate(todos):
    print(f'{v:<4}{c[0]:>8}{c[3]:>8}\n')

while True:
    perm = int(input('Deseja ver as notas de algum aluno?[999] para sair'))
    if perm <= len(todos)-1:
        print(f'Nota 1:{todos[perm][1]}\nNota 2:{todos[perm][2]}')
    if perm == 999:
        break


### precisa dar um clear nesse codigo
