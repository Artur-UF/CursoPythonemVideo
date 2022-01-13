# fatorial
n = int(input('Digite um número: '))
f = 1
n1 = n
'''while n >= 1:
    f *= n
    n -= 1
print('O fatorial de {} é: {}'.format(n1, f))
'''
f1 = 1
for c in range(n1, 0, -1):
    f1 *= c
print('O fatorial de {} é: {}'.format(n1, f1))
