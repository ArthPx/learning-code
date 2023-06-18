import random
a= input('Qual é o nome do primeiro aluno? ')
b= input('Qual é o nome do segundo aluno? ')
c= input('Qual é o nome do terceiro aluno? ')
d= input('Qual é o nome do quarto aluno? ')
r1= (a,b,c,d)
e= random.choice(r1) 
print('O escolhido é {}'.format(e))



