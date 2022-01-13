# PA otimizada
n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 0
print('Os 10 primeiros termos da PA são:')
while c < 10:
    print(n, end=' ')
    n += r
    c += 1
