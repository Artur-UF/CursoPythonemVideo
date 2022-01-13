from random import choice
n = int(input('Escolha um número entre 0-5: '))
l = choice([0, 1, 2, 3, 4, 5])
if n==l:
    print('Você acertou!')
else:
    print('Errou, burro! o número certo era {}'.format(l))
