import random
a= input('Nome de um aluno ')
b= input('Nome de um aluno ')
c= input('Nome de um aluno ')
d= input('Nome de um aluno ')
r1 = [a,b,c,d]
r= random.shuffle(r1)
print('A ordem de apresentação será\n {}'.format(r1))
