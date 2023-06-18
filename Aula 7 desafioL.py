km= float(input('Quantos km o carro percorreu? '))
dias= int(input('Quantos dias você ficou com o carro? '))
vdias= dias*60
vkm= km*0.15
print('O valor total a pagar é R${:.2f}'.format(vdias+vkm))
