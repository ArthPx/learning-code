'''
fc = list()
ab = list()
exp = str(input('Digite a expressão:'))
for c in exp:
    if '('in c:
        ab.append('(')
    if ')' in c:
        fc.append(')')       #jeito q eu fiz q está errado.
if ab.count('(') == fc.count(')'):
    print('A expressão está valida')
else:
    print('A expressão está invalida')
'''

exp = str(input('Digite a expressão:'))

pilha = []
for c in exp:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) > 0:
    print('A sentença está Inválida')
elif len(pilha) == 0:
    print('A sentença está Válida')

