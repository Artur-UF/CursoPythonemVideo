s = 0
for c in range(0, 6, 1):
    n = int(input('Número: '))
    if n % 2 == 0:
        s += n
print('O somatório dos pares é: {}'.format(s))
