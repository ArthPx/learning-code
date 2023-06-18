a= int(input('Digite o primeiro valor '))
b= int(input('Digite o segundo valor '))

if a<b:
    maior=b
    menor=a
    print('{} é o segundo valor e é o maior e {} é o primeiro valor e é o menor'.format(b,a))
if a>b:
    maior=a
    menor=b
    print('{} é o primeiro valor e é o maior e {} é o segundo valor e é menor'.format(a,b))
elif a==b:
    print('{} e {} são valores iguais!'.format(a,b))





