from random import randint
jogos = [[]]
count = 0
palpites = int(input('Quantos palpites serão gerados?: '))
while count <= palpites:
    for c in jogos:
        count += 1
    for v in range (0,6):
        r = randint(1,60)
        while r in jogos[c]:
            r = randint
        jogos.append(r)
               
print('=-'*30)
print('Jogos gerados:')


