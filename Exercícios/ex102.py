# fatorial chic
def fatorial(n, show=False):
    """
    ==> Essa função calcula o fatorial de um número.
    :param n: é o parametro a ser calculado o fatorial
    :param show: se True faz print do processo
    :return: retorna o resultado
    """
    if show:
        f = 1
        for v in range(n, 0, -1):
            print(f'{v}', end=' ')
            f *= v
            if v == 1:
                print('= ', end='')
                break
            print('x', end=' ')
        return f
    else:
        f = 1
        for v in range(n, 0, -1):
            f *= v
        return f


n = int(input('Quero o fatorial do número: '))
print(fatorial(n))
