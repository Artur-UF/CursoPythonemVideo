# menu help
from time import sleep


def escrevav(msg):
    n = len(msg)+4
    print('\033[m\033[1:42m='*n)
    print(f'\033[1:42m{"":2}{msg}{"":2}')
    print('\033[1:42m='*n, end='\n\033[m')


def escrevaa(msg):
    n = len(msg)+4
    print('\033[1:44m='*n)
    print(f'\033[1:44m{"":2}{msg}{"":2}')
    print('\033[1:44m='*n, end='\n\033[m\033[7:40m')


he = 'oi'
while True:
    escrevav('Sistema de ajuda PyHelp')
    he = input('Função ou biblioteca > ')
    if he in 'Fimfim':
        break
    escrevaa(f'Acessando namual do comando {he}')
    sleep(0.8)
    help(he)
    sleep(2)
