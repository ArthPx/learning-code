print('-=-'*20)
km= int(input('Qual é a velocidade do carro? '))
if km > 80:
    print('Voce ultrapassou o limite da via de 80km/h !!! Será multado em R${:.2f}'.format((km-80)*7))
else:
    print('Voce passou no radar dentro do limite! Parabéns!')
print('-=-'*20)

