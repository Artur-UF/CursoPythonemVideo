def aumentar(v, p, form=False):
    if form:
        return f'R${v*(1+(p/100)):.2f}'
    else:
        return v*(1+(p/100))


def diminuir(v, p, form=False):
    if form:
        return f'R${v * (1 - (p / 100)):.2f}'
    else:
        return v * (1 - (p / 100))


def metade(val, form=False):
    if form:
        return f'R${val / 2}'
    else:
        return val/2


def dobro(val, form=False):
    if form:
        return f'R${val * 2}'
    else:
        return val*2


def moeda(n):
    return f'R${n:.2f}'


def resumo(val, au, di):
    print('-'*30)
    print(f'{"Resumo do valor":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<18}R${val:.2f}')
    print(f'{"Dobro do preço:":<18}R${val*2:.2f}')
    print(f'{"Metade do preço:":<18}R${val/2:.2f}')
    print(f'{f"{au}% de aumento:":<18}R${val*((100+au)/100):.2f}')
    print(f'{f"{di}% de desconto:":<18}R${val*((100-di)/100):.2f}')
    print('-'*30)
