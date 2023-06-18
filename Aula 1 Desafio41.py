from datetime import date
ano = int(input('Qual é o ano de nascimento do sujeito? '))
hoje= date.today().year
idade= hoje - ano
if idade <=9:
    print(f'O Competidor tem {idade} anos e pertence a categoria \033[34m[Mirim]\033[m')
elif idade <=14:
    print(f'O Competidor tem {idade} anos e pertence a categoria \033[32m[Infantil]\033[m')
elif idade <=19:
    print(f'O Competidor tem {idade} anos e pertence a categoria \033[36m[Júnior]\033[m')
elif idade <=25:
    print(f'O Competidor tem {idade} anos e pertence a categoria \033[35m[Senior]\033[m')
else:
    print(f'O Competidor tem {idade} anos e pertence a categoria \033[31m[Master]\033[m')