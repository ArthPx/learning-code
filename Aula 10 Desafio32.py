ano= int(input('Escreva um ano e descubra se ele é bissexto!'))
bissexto= ano % 4 == 0 and ano%100 != 0 or ano%400 == 0
if bissexto:
    print('O ano(s) {} é Bissexto'.format(ano))
else:
    print('O ano(s) {} não é Bissexto'.format(ano))
