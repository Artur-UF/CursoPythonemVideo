print('A soma de todos múltiplos de 3 ímpares entre 1-500', end=' ')
n = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += c
print('é: {}'.format(n))
