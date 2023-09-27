tupla = ('serio','bravo','triste','chateado','feliz','felicidade','intristecido')
for t in tupla:
    print(f'\nNa palavra {t} temos: ',end='')
    for p in t:
        if p.lower() in 'aeiou':
            print(f'{p} ',end='')

