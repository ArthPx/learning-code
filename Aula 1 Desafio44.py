produto= float(input('Qual o valor do produto? '))

metodo= float(input('Como você irá pagar?\n [1] À vista Dinheiro ou cheque(10% de desconto)\n [2] À vista no cartão (5% de desconto) \n [3] Em até 2x no cartão (Preço do produto)\n [4] 3x ou mais no cartão (20% juros)\n Qual é a opção?..:'))
dinheiro= (produto/100)*10
avcartao= (produto/100)*5
juros=    (produto/100)*20

if metodo==1:
    print(f'A compra ficará em R${produto-dinheiro:.2f}')
    pagar=int(input('Deseja finalizar a compra? [1] SIM [2] NÃO\n ..:'))
    if pagar == 1:
        print(f'Compra finalizada com sucesso! no valor de R${produto-dinheiro:.2f}, Espero você novamente !! ')
    else:
        print(f'Compra negada com Sucesso')
elif metodo==2:
    print(f'A compra ficara em {produto-avcartao:.2f}')
    pagar=int(input('Deseja finalizar a compra? [1] SIM [2] NÃO\n ..:'))
    if pagar ==1:
        print(f'Compra realizada com sucesso!! No valor de R${produto-avcartao:.2f}, Espero você novamente !!')
    else:
        print(f'Compra negada com Sucesso')
elif metodo==3:
    print(f'A compra ficará em R${produto:.2f}')
    pagar= int(input('Deseja finalizar a compra? [1] SIM [2] NÃO\n ..:'))
    if pagar==1:
        print(f'Compra realizada com sucesso !! No valor de R${produto:.2f}, Espero você novamente !! ')
    else:
        print('Compra negada com Sucesso')
else:
    print(f'A Compra ficará em R${produto+juros:.2f}')
    pagar= int(input('Deseja finalizar a compra? [1] SIM [2] NÃO\n ..:'))
    if pagar==1:
        print(f'Compra finalizada com Sucesso !! No valor de {produto+juros:.2f}, Espero você novamente !!')
    else:
        print('Compra negada com sucesso')

    



        



