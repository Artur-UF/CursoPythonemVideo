# jogador
stats = {'Nome': input('Nome: '), 'gols':[], 'total':0}
r = int(input('Quantas partidas ele jogou? '))
for c in range(0, r):
    g = int(input(f'Quantos gols na partida {c+1}? '))
    stats['gols'].append(g)
    stats['total'] += g
print(stats)
print('=-'*20)
for k, v in stats.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*20)
print(f'O jogador {stats["Nome"]} jogou {r} partidas.')
for c in range(0, r):
    print(' '*3, f'=>Na partida {c+1}, fez {stats["gols"][c]} gols.')
print(f'No total fez {stats["total"]} gols.')  # se fizer sum() e botar a lista de gols da tmb
