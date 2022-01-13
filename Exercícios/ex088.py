# MEGA SENA
from random import randint
n = int(input('Quantos jogos você quer? '))
ap = []
for c in range(0, n):
    while len(ap) != 6:
        v = randint(1, 60)
        if v not in ap:
            ap.append(v)
    print(f'Jogo {c+1}: {sorted(ap)}')
    ap.clear()
