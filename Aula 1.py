nome = str(input('Qual é o seu nome? ')).upper().strip()
if nome == 'GUSTAVO':
    print('Que nome bonito !')
elif nome== 'PEDRO' or nome== 'MARIA' or nome== 'JOÃO':
    print('Seu nome é normal..')
else:
    print('Seu nome é meio pah..')
print('Tenha um bom dia {}'.format(nome))