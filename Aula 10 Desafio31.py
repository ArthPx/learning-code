km= float(input('Quantos km é a sua viagem? '))
normal= 0.5*km
maior= 0.45*km
if km < 200:
    print('Você irá pagar R${} pela viagem!'.format(normal))
else:
    print('Você irá pagar R${} pela viagem com o desconto de km!'.format(maior))