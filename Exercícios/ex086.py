# matriz?
'''mtz = []
n = []
for c in range(0,9):
    mtz.append(int(input('Digite um número: ')))
print(f'[ {mtz[0]} ][ {mtz[1]} ][ {mtz[2]} ]\n[ {mtz[3]} ][ {mtz[4]} ][ {mtz[5]} ]\n[ {mtz[6]} ][ {mtz[7]} ][ {mtz[8]} ]')
s = 0
for c in range(2, 9, 3):
    s += mtz[c]
print(f'A soma da terceira coluna é: {s}')
sp = 0
for c in mtz:
    if c % 2 == 0:
      sp += c
print(f'A soma dos valores pares é: {sp}')
print(f'O maior valor da segunda linha é: {max(mtz[3:6])}')'''
# Outra maneira de fazer a matriz:
mtz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        mtz[l][c] = int(input(f'Digite o valor da posição [{l+1}, {c+1}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mtz[l][c]:^5}]', end='')
    print()
