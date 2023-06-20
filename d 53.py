# PALINDROMO É UMA FRASE OU PALAVRA QUE SE LIDA AO CONTRARIO DÁ O MESMO RESULTADO
pal = str(input('Digite a frase ou palavra:.')).strip().upper()
palavras = pal.split()
junto = "".join(palavras)   
inverso = junto[::-1]
if junto == inverso:
    print(f'{pal} é um palindromo')
else:
    print(f'{pal} não é um palindromo')
