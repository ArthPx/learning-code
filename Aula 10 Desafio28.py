import random
resposta= int(input('Escolha um numero inteiro entre 0 e 5 '))
escolhas = (1,2,3,4,)
poggers = random.choice(escolhas)
if resposta == poggers:
    print('Você acertou é {}'.format(resposta))
else:
    print('Você errou !! era {}'.format(poggers))

