# dados
from random import randint
from time import sleep
from operator import itemgetter
'''jg = {'Jogadores':[], 'valor':[]}
for c in range(0, 4):
    jg['valor'].append(randint(1, 6))
    jg['Jogadores'].append(f'Jogador{c+1}')
    print(f'O jogador{c+1} tirou {jg["valor"][c]}')
    sleep(0.5)
for v in range(0, 4):
    print(f'Em {v+1}º lugar ficou o {jg["Jogadores"][jg["valor"].index(sorted(jg["valor"])[-(v+1)])]} que tirou {sorted(jg["valor"])[-(v+1)]}')
    sleep(0.5)'''
jogo = {'jogador1': randint(0, 6),
        'jogador2': randint(0, 6),
        'jogador3': randint(0, 6),
        'jogador4': randint(0, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
# daí é só botar um frufru