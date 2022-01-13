# PAR ou ÍMPAR
from random import randint
cont = 0
while True:
    n = int(input('Diga um valor: '))
    pi = input('Você quer par ou ímpar [P/I] ? ').lower()
    comp = randint(1, 10)
    soma = n + comp
    if soma % 2 == 0:
        if pi == 'p':
            print(f'Você ganhou, você escolheu {n} e o computador escolheu {comp} e a soma é {soma}')
            cont += 1
        elif pi == 'i':
            print(f'Você perdeu, o computador escolheu {comp} e você escolheu {n} e a soma é {soma}')
            print(f'Você ganhou {cont} rodadas.')
            break
    else:
        if pi == 'i':
            print(f'Você ganhou, você escolheu {n} e o computador escolheu {comp} e a soma é {soma}')
            cont += 1
        else:
            print(f'Você perdeu, o computador escolheu {comp} e você escolheu {n} e a soma é {soma}')
            print(f'Você ganhou {cont} rodadas.')
            break
