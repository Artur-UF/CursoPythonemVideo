# tabuada
n = int(input('De qual tabuada você precisa? '))
print('='*15)
for c in range(1, 11, 1):
    print(''*3, '{} x {:2}= {}'.format(n, c, n*c))
print('='*15)
