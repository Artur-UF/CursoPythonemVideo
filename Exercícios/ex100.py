# sorteio
from random import choices
from time import sleep


def sorteia(list):
    print('Sorteando 5 elementos da lista temos:', end=' ')
    n = choices(list, k=5)
    for c in n:
        print(c, end=' ')
        sleep(0.3)
    print('Fim!')
    list.clear()
    for c in n:
        list.append(c)


def sopar(list):
    print(f'A soma dos números pares da seguinte lista {list} é:', end=' ')
    s = 0
    for c in list:
        if c % 2 == 0:
            s += c
    print(f'{s} FIM!')


nums = []
for c in range(1, 11):
    nums.append(c)
sorteia(nums)
print(nums)
sopar(nums)
