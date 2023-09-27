times =('botafogo', 'palmeiras',
'gremio', 'flamengo','fluminense',
'bragantino','athletico-pr', 'fortaleza',
'ATLETICO -MG','cuiaba','sao paulo','Cruzeiro',
'Corinthians','Internacional','Goiás','Bahia',
'Santos','Vasco da gama','américa-mg','coritiba')
print('Cinco primeiros times do brasileirão')
print(times[:5])
print('Os ultimos 4 colocados')
print(times[-4:])
print('Em ordem alfabetica')
print(sorted(times))
print('Em que posição está o cruzeiro?')
pos = times.index("Cruzeiro")
print(f'Está em {pos + 1}º lugar')
