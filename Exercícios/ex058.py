# jogo de adivinhação
from random import randint
co = randint(1, 10)
eu = int(input('Digite um número de 1-10: '))
te = 1
while eu != co:
    eu = int(input('Errou, o computador pensou em {}, tente novamente: '.format(co)))
    co = randint(1, 10)
    te += 1
print('parabéns você acertou, o computador pensou em {} e você teve {} tentativas'.format(co, te))
