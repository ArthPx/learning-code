import math
o= float(input('Digite o valor do cateto oposto '))
a= float(input('digite o valor do cateto adjacente '))
# o² + a² = h²
h= math.sqrt((o**2) + (a**2))
print('O valor da hipotenusa é {}'.format(h) )

