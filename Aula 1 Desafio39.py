from datetime import date
atual= date.today().year
nasc= int(input('Qual ano você nasceu? '))
dter= atual - 18 - nasc
vter= (atual-18-nasc)*-1
if nasc == atual-18:
    print('Você deve se alistar esse ano!' )
elif atual-18>nasc:
    print('Você deveria ter se alistado a {} atrás'.format(dter))
elif atual-18<nasc:
    print('Você tem que se alistar daqui {} anos'.format(vter))
 #CORRETO
