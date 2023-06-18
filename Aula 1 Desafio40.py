n1= float(input('Qual a primeira nota? '))
n2= float(input('Qual a segunda nota? '))
media= (n1+n2)/2
if media<5.0:
    print('Voce teve uma media de \033[31m[{}]\033[m e foi \033[31mReprovado\033[m!'.format(media))
elif media>=5.0 and media<6.9:
    print('Você teve uma media de \033[33m[{}]\033[m e entrou em \033[33mRecuperação\033[m! Procure o professor para mais informações'.format(media))
else:
    print('Você passou de ano, parabéns teve uma media superior a \033[36m6.0!!\033[m Nota atual \033[36m[{}]\033[m'.format(media))
