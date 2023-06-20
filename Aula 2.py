#n= int(input('Digite um número '))
#for c in range(0,n):
 #   print(c)
#print('FIM')

#i = int(input('Inicio: '))
#f= int(input('Fim: '))
#p= int(input('Passo: '))
#for c in range(i,f,p):
#    print(c)
#print('FIM')

#for c in range (0,3):
#    n= int(input('Digite um valor: '))
#print('Fim')
s=0
v=1
p= int(input('Você quer somar, ou multiplicar?\n [0] SOMAR\n [1] MULTIPLICAR '))
if p==0:
    for c in range (0,3):
        n= int(input('Digite um valor..'))
        s+=n
    
    print(f'O valor total da soma é {s} ..:')
elif p==1:
    for c in range(0,3):
        n= int(input('Digite um valor.. '))
        v = v*n
    print(f'O valor total é {v}')


