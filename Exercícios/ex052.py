# é primo?
n = int(input('Digite um número: '))
di = []
for c in range(2, n):
    if n % c == 0:
        di.append(c)
if not di:
    print('É primo.')
else:
    print('Não é primo e esses são seus divisores: {}'.format(di))
