# maior DE NOVO
from time import sleep


def maior(*val):
    print('=-'*(len(val)+25))
    for c in val:
        print(c, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(val)} valores e o maior é o {max(val)}')
    print('=-' * (len(val) + 25))


maior(3, 5, 2, 6, 8, 3, 9, 0)
maior(0, 2, 5, 1, 7, 4)