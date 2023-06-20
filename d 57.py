'''s = str(input('Sexo [M/F]:')).strip().upper()[0]
if s in 'Ff':
    print('Sexo Feminino Registrado com sucesso !')
elif s in 'Mm':
    print('Sexo Masculino Registrado com sucesso !')
while s not in 'FfMm':
    s = str(input('Sexo invalido. Porfavor insira seu sexo correto! [M/F]')).strip().upper()[0]
    if s in 'Ff':
        print('Sexo Feminino Registrado com sucesso !')
    elif s in 'Mm':
        print('Sexo Masculino Registrado com sucesso ! ')
'''
s= str(input('Sexo [M/F]:')).strip().upper()[0]
while s not in 'FM':
    s= str(input('Sexo Invalido, digite novamente [M/F]:')).strip().upper()[0]
print(f'Sexo [{s}] registrado com sucesso!')


