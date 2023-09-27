soma = 0
count = 0
menor = 0
nmenor = ""
counti = 0
p = "S"
while p not in 'Nn':
    counti  += 1
    n=str(input('Nome:'))
    preco=int(input('Preço:'))
    soma += preco
    p=str(input('Deseja Adicionar mais produtos? [S/N]')).upper()
    if preco> 1000:
        count += 1
    if counti == 1:
        menor = preco
        nmenor = n
    if counti > 1:
        if preco < menor:
            menor = preco
            nmenor = n
print(f'Total gasto: R${soma:.2F}\nProdutos Acima de R$1000: {count}\nProduto mais barato: {nmenor}')

        





    



    
