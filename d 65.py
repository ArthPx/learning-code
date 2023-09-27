p = 'S'
soma = quant = media= 0
quant = 0
n=0
while p in 'Ss' : 
    n= int(input('Digite um numero:'))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n>maior:        # se o maior numero que eu acabei de digitar for maior q o antigo maior, o novo numero é o maior
            maior = n
        if n<menor: #mesma coisa do de cima soq ao contrario
            menor = n 
    p = str(input('Deseja continuar? [S/N]:')).upper().strip()
media = soma/quant
print(f'A media é {media} o Maior é {maior} o Menor é {menor} ') 




    