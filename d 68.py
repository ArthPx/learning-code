from random import randint
n = 1
compdec = ""
compn= 0
soma = 0
cont = 0
print('Jogo de par ou impar com o computador')
while n != 0:
    n = int(input('Diga um valor entre 1 e 10:'))
    dec = str(input('Selecione [P/I]:')).upper()
    if dec == "P":
        compdec == "I"
    else:
        compdec == "P"
    compdec = randint(0,10)
    print(f'O computador escolheu {compdec}')

    soma = compdec + n
    print(f'A soma entre {n} + {compdec} é {soma}')
    if soma % 2 == 0:
        if dec == "P":
            print('Voce Ganhou ! vamos tentar novamente...')
            cont +=1
        elif dec == "I":
            print('Voce Perdeu ! Esses foram seus resultados')
            print(f"{cont} partidas vencidas consecutivamente")
    else:
        if dec == "I":
            print('Voce Ganhou ! vamos tentar novamente...')
            cont +=1
        elif dec == "P":
            print('Voce Perdeu ! Esses foram seus resultados')
            print(f"{cont} partidas vencidas consecutivamente")
            break




    

