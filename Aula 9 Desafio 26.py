frase= str(input('Digite uma frase qualquer ')).upper()
#print(len(frase))
#print(frase.count('A'))
#print(frase.rfind('A'))
#print(frase.find('A'))

print('Quantas vezes a letra " a ou A " aparece na frase? {}\n Em qual posição na primeira vez? {}\n E a ultima vez? {} '.format(frase.count('A'),frase.find('A'),frase.rfind('A')))