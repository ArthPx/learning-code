
num= float(input('Digite um numero para ver sua tabuada '))
tab = int(input('Digite até quando vocÊ quer ver a tabuada (ex: até 7, até 10)'))
for c in range(1,tab + 1):
    print(f' {num} x {c} = {num*c}')


