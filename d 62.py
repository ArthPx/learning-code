ptermo = int(input('Digite o primeiro termo '))
raz = int(input('Digite a razão '))
tot = ptermo
s=1
total = 0
perg =10
while perg != 0:
    total += perg
    while s <= total:
        print(f'{tot} → ',end='')
        tot += raz
        s += 1
    perg = int(input('Você quer ver quantos mais termos? 0 para encerrar o programa '))




