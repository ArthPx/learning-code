comidade=0

maisdevinteanosmulher=0
maior=0
maioridadehomem=""
for p in range (1,5):
    print('--------{}ª Pessoa--------'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo M/F:')).strip()
    comidade += idade
    if sexo in 'Mm'.strip():
        if  idade > maior:
            maior = idade
            maioridadehomem = nome
            
    if sexo in 'Ff'.strip():
        if idade >= 20:
            maisdevinteanosmulher+= 1

                
media = comidade/4

print(f'A media do grupo é {media}')
print(f'{maioridadehomem} é o homem mais velho do grupo, e tem {maior} anos')
print(f'E temos {maisdevinteanosmulher} mulheres a cima de 20 anos')

