# pessoas leves e pesadas
go = []
ma = []
pe = []
while True:
    n = input('Nome: ')
    p = float(input('Peso: '))
    if p >= 100:
        pe.append(n)
        pe.append(p)
        go.append(pe[:])
        pe.clear()
    elif p <= 70:
        pe.append(n)
        pe.append(p)
        ma.append(pe[:])
        pe.clear()
    r = input('Quer continuar? [S/N] ').strip().lower()[0]
    while r != 's' and r != 'n':
        r = input('Quer continuar? [S/N] ').strip().lower()[0]
    if r in 'n':
        break
print(f'Você registrou {len(go)+len(ma)}')
print(f'As pessoas com/mais de 100kg é/são:', end=' ')
for c in range(0, len(go)):
    print(f'{go[c][0]}...', end='')
print(f'\nAs pessoas com/menos de 70kg é/são:', end=' ')
for c in range(0, len(ma)):
    print(f'{ma[c][0]}...', end='')
