peso= float(input('Qual é o seu peso? '))
altura= float(input('Qual é a sua altura? '))
formula = peso/(altura**2)
if formula>18.5 and formula<25:
    print(f'Seu IMC é {formula:.2f} e você está no seu peso ideal! ')
elif formula>25 and formula<30:
    print(f'Seu IMC é {formula:.2f} e você está  com sobrepeso! ')
elif formula>30 and formula<40:
    print(f'Seu IMC é {formula:.2f} e você está em situação de obesidade! ')
elif formula<18.5:
    print(f'Seu imc está baixo, faz um bulking po')
else:
    print(f'Seu IMC é {formula:.2f} e você está em situação de \033[31mobesidade morbida!!\033[m ')
