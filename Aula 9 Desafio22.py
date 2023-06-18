nome= str(input('Qual o seu nome?')).strip()
dividido = nome.split()
print(' Seu nome com as letras maiusculas {}\n Minúsculas {}\n Quantas letras ao todo sem espaços {}\n Quantas letras no primeiro nome {}'.format(nome.upper(),nome.lower(),len(nome) - nome.count(' '),len(nome.split() [0])))

