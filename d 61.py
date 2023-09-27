pterm = int(input('Primeiro termo da PA '))
raz = int(input('Razão da PA '))
cont= 0
tot = pterm
while cont<10:
    print(f'→ {tot} ',end='')
    tot += raz
    cont += 1
