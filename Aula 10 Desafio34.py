salario= float(input('Qual o seu salario? '))


if salario<=1250:
    novo = salario + (salario/100)*15
else:
   novo= salario + (salario/100)*15
print('\033[7;36;47mQuem ganhava R${:.2f} passa a ganhar R${:.2f}\033[m'.format(salario,novo))
