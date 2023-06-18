nome= str(input('Escreva um nome qualquer? ')).strip()
n= nome.split()
print('Seu nome {}\n Primeiro nome {}\n Ultimo nome {}'.format(nome,n[0],n[-1]))