#JOKENPO
from random import randint
import time
print('\033[36m-=-\033[m'*20)
itens= ('\033[37mPedra\033[m','\033[33mPapel\033[m','\033[34mTesoura\033[m')
jogada= int(input(f'Qual jogada você irá fazer?\n [0]{itens[0]}\n [1]{itens[1]}\n [2]{itens[2]}\n ..:'))
pc= randint(0,2)

print(itens[0])
time.sleep(1)
print(itens[1])
time.sleep(1)
print(itens[2])
time.sleep(1)

print(f'O JOGADOR JOGOU {itens[pc]}')
time.sleep(0.5)
print(f'O COMPUTADOR JOGOU {itens[jogada]}')

if pc == 0:
    if jogada == 1:
        time.sleep(1)
        print('O Jogador ganhou !')
    elif jogada == 2:
        time.sleep(1)
        print('O Computador Venceu !!')
    else:
        print('O Jogo deu empate...')
if pc == 1:
    if jogada == 0:
        time.sleep(1)
        print('O Computador venceu !!')
    elif jogada == 1:
        time.sleep(1)
        print('O Jogador ganhou!!')
    else:
        time.sleep(1)
        print('O jogo deu empate...')

if pc == 2:
    if jogada == 0:
        time.sleep(1)
        print('O Jogador ganhou!!')
    elif jogada ==1:
        time.sleep(1)
        print('O Computador ganhou!!')
    else:
        print('O jogo deu empate...')
print('\033[36m-=-\033[m'*20)






    
