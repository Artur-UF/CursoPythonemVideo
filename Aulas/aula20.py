# funções
def lin():
    print('-'*30)


def tit(msg):
    print('-'*(len(msg)+4))
    print(f'  {msg}')
    print('-'*(len(msg)+4))


def soma(a, b):
    print(a+b)


def dobra(lst):
    for c in range(0, len(lst)):
        lst[c] *= 2
    print(lst)


def so(*nums):    # * forma uma tupla com argumentos
    tit(nums)
    s = 0
    for c in nums:
        s += c
    print(f'A soma dos valores é: {s}')


def kw(**kwargs):  # ** forma um dicionário com argumentos
    print(kwargs)
    for k in kwargs:
        print(f'A chave é {k} e o valor atribuído é: {kwargs[k]}')


lin()
print('Aula de Funções')
lin()
tit('Título')
soma(5, 6)
lin()
valores = [4, 3, 7, 2]
dobra(valores)
lin()
so(4, 7, 1, 5, 9, 12)
kw(Nome='Artur', Sobrenome='Uhlik Frohlich', Idade=20)
