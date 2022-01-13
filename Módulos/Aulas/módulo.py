def fatorial(no):
    f = 1
    for c in range(1, no+1):
        f *= c
    return f


def raiz(n, rad=2):
    """Use o parâmetro rad para indicar o radical, se não indicar será
    calculada a raiz quadrada"""
    return n**(1/rad)
