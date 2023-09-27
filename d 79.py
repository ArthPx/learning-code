c = 's'
nums = list()
while c == 's':
    nums.append(int(input('Valor:')))
    if nums[-1] in nums[0:-1]:
        nums.pop()
        print('ERROR! Valor já adicionado, tente novamente')   
    else:
        print('VALOR ADICIONADO COM SUCESSO!') 
    c = str(input('Quer continuar?[S/N]')).lower().strip()[0]
print(f'Os valores digitados foram\n{sorted(nums)}')




        
        


