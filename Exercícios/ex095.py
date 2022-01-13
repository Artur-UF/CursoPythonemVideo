# aprimore o 093
jgs = []
while True:
    stats = {'Nome': input('Nome: '), 'gols':[], 'total':0}
    r = int(input('Quantas partidas ele jogou? '))
    for c in range(0, r):
        g = int(input(f'Quantos gols na partida {c+1}? '))
        stats['gols'].append(g)
        stats['total'] += g
    jgs.append(stats)
    perg = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while perg != 's' and perg != 'n':
        perg = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if perg in 'n':
        break

print('=-'*30)
print(f'{"|No.":>4}{"|Nome":<7}{"|Gols":<20}{"|Total":<5}')
print('-'*35)
for po, j, in enumerate(jgs):
    print(f'{po:<4}{j["Nome"]:<7}{str(j["gols"]):<20}{j["total"]:<5}')
print('-'*35)
while True:
    r1 = int(input('Quer ver as informações de qual jogador? [No.](999 para fechar): '))
    if r1 == 999:
        break
    if 0 <= r1 <= (len(jgs)-1):
        print(f'Os dados do jogador {jgs[r1]["Nome"]} são:\n{jgs[r1]}')
        print('='*30)
    else:
        print('Índice de jogador não registrado.')
print('Tchau :)')