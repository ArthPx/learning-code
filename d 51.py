
ptermo= int(input('Digite o primeiro termo:. '))
razão= int(input('Digite a razão dessa p.a:. '))
décimo= ptermo + (11-1) * razão

print('A P.A desse numero com essa razão é a seguinte')
for c in range (ptermo,décimo, razão):
    
   print(f'{c}', end= " -> ")