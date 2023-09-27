numeros = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
pos = 0
while True:
    perg = int(input('Digite um número entre 0 e 20:'))
    if 0 <= perg <= 20:
        break
    print('Tente Novamente.',end=' ')
pos = perg
print(f'Você digitou o numero {numeros[pos]}')