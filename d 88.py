from random import randint
from time import sleep
jogos = []
dados = []
count = 1
palpites = int(input('Quantos palpites serão gerados?: '))
while count <= palpites:
    for v in range(1,7):
        re = randint(1,60)
        while re in jogos:
            re= randint(1,60)
        if re not in jogos:
            jogos.append(re)
    count += 1
    dados.append(jogos[:])
    jogos.clear()     
print(f'=-'*15,'Sorteando os jogos','=-'*15)
for c in range (0,palpites):
    print(f'Jogo {c + 1}: {dados[c]}')
    sleep(1)
print('=-' * 50)

