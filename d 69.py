p = 'S'
conti = 0
contm = 0
contfi = 0 
while p != 'N':
    i= int(input('Idade:'))
    sex= str(input('Sexo [M/F]:')).upper()
    if sex not in 'MFfm':
        sex= str(input('Sexo [M/F]:')).upper()
    if i >= 18:
        conti +=1
    if sex == "M":
        contm  += 1
    if sex == "F":
        if i <20:
            contfi += 1
    p= str(input('Quer continuar?[S/N]:')).upper().strip()
print(f" Pessoas acima de 18 anos {conti}\n Homens cadastrados {contm}\n Mulheres menores de 20 anos {contfi}")




