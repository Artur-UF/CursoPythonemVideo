# contagem
from time import sleep


def escreva(msg):
    n = len(msg)+4
    print('='*n)
    print(f'{"":2}{msg}{"":2}')
    print('='*n)


def cont(a1, an, r):
    if a1 < an:
        if r == 0:
            r = 1
        for c in range(a1, (an+1), r):
            print(c, end=' ')
            sleep(0.3)
        print(' FIM!')
    else:
        if r == 0:
            r = 1
        elif r < 0:
            r *= -1
        for c in range(a1, (an-1), -r):
            print(c, end=' ')
            sleep(0.3)
        print(' FIM!')


escreva('Contador')
cont(1, 10, 1)
cont(10, 1, 1)
cont(int(input('De: ')), int(input('Até: ')), int(input('A cada: ')))
