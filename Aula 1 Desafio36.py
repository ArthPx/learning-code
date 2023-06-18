valor= float(input('Qual o valor da casa? R$'))
salário= float(input('Qual o salario do comprador ? R$'))
anos= int(input('Em quantos anos ele irá quitar a casa? R$'))
psalario= (salário/100)*30
mensal= anos*12
print('Será R${:.2f} mensalmente'.format(valor/mensal))
if valor/mensal >= psalario:
    print('Infelizmente o valor de R${:.2f} foi negado pelo banco..'.format(valor))
else:
    print('O emprestimo bancario foi realizado com sucesso!')
#Correto