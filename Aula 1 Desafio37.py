num= int(input('\033[35mDigite um numero '))
print ('\033[36m-=-'*20)
pgt = int(input('Você quer transformar {} em\n [1] Binario\n [2] Hexadecimal\n [3] Octal ?\n Digite..: '.format(num)))
print('-=-'*20)
if pgt == 1:
    bina = str(bin(num))
    print('O numero em binario é \033[35m{}\033[36m'.format(bina))
elif pgt == 2:
    hexa = str(hex(num))
    print('O numero em hexadecimal é \033[35m{}\033[36m'.format(hexa))
elif pgt == 3:
    octal = str(oct(num))
    print('O numero em octal é \033[35m{}\033[36m'.format(octal))
print('-=-'*20)
#CORRETO


