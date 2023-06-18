r1= float(input('Qual o comprimento de r1? '))
r2= float(input('Qual o comprimento de r2? '))
r3= float(input('Qual o comprimento de r3? '))
#um de seus lados deve ser maior que o valor absoluto (módulo)
#da diferença dos outros dois lados e menor que a soma dos outros dois lados

if r1 > r2-r3 and r2> r1-r3 and r3> r2-r1:
    print('Pode ser formado um triangulo !')
else:
    print(' Não pode ser formado um triangulo com esses valores..')

