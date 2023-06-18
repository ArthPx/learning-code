
print('-='*10,'Caculadora','-='*10)
ope=0
op=True
num1= int(input('Digite um número desejado:'))
num2= int(input('Digite um segundo número desejado:'))
while op is True:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa' )
    ope= int(input('Qual a opção desejada? '))
    if ope == 1:
        print(f'O resultado da soma dos dois números é {num1+num2}')
    elif ope == 2:
        print(f'O resultado da Multiplicação dos dois números é {num1+num2}')
    elif ope == 3:
        if num1 > num2:
            print(f'O {num1} é maior que o {num2}')
        elif num2 > num1:
            print(f'O {num2} é maior que o {num1}')
        else:
            print(f'Os dois valores são iguais')
    elif ope == 4:
        num1 = int(input('Digite um novo numero:'))
        num2 = int(input('Digite um novo segundo número:'))
    elif ope not in [1,2,3,4,5]:
        print('Essa nao é uma das alternativas, tente novamente!')
    else:
        print('Tchauzinho!')
        op = False


