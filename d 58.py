import random
import time
s = 1
print('Irei pensar em um numero entre 1,10, tente adivinhar !')
print('Pensando ...')
time.sleep(1)
print('.')
time.sleep(1)
print('..')
time.sleep(1)
print('...')
time.sleep(1)
pens =random.randint(1,10)
perg = int(input('Pensei ! Tente adivinhar:'))
while perg != pens:
    if perg<pens:
        print('')
        perg = int(input('É mais,tenta denovo ai bobão: '))
    elif perg > pens:
        perg = int(input('É menos, tenta denovo ai bobão:'))
    s += 1
print('...')
time.sleep(1)
print('Parabéns !!!')
print(f'Você acertou !!! a resposta era {pens}')
print(f'Foram necessarios {s} Palpites para vencer')
