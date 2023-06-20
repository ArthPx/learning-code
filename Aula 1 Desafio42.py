#'''um de seus lados deve ser maior que o valor absoluto (módulo)
# da diferença dos outros dois lados e menor que a soma dos outros dois lados
l1= float(input('Insira um lado do triangulo..:'))
l2 = float(input('Insira outro lado do triangulo..:'))
l3 = float(input('Insira outro lado do triangulo..:'))
if l1> l2-l1 and l2>l1-l2 and l3>l2-l1:
    if l1 != l2 != l3 !=l1:
        print('Você tem um triangulo Escaleno')
    elif l1 == l2 == l3:
        print('Esse triangulo é Equilatero!')
    else:
        print('Esse triangulo é Isosceles')
else:
    print('Os lados digitados não formam um triangulo!')

