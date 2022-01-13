# Funções p2
def escreva(msg):
    """
    Isso produz uma mensagem centralizada entre linhas feitas de iguais
    :param msg: escreva uma mensagem
    :return: sem retorno
    """
    n = len(msg)+4
    print('='*n)
    print(f'{"":2}{msg}{"":2}')
    print('='*n)


def somar(a, b, c=0):
    """
    => aí o c é opcional, se não for declarado vai ser assumido 0
    :param a: int
    :param b: int
    :param c: int
    :return: a função retorna a soma s, ou seja, podemos usar o somar() como um valor
    """
    s = a + b + c
    return s


''' Variáveis declaradas dentro de defs só são válidas localmente
    e as declaradas fora de defs são válidas globalmente, mas se eu 
    quiser que uma varável declarada dentro de uma def seja válida coloque ela depois de um global _'''
def teste():
    global b
    b = 4
    a = 3
    print(f'a dentro é {a}')
    print(f'b dentro é {b}')


'''help(print)  # mostra tutoriais sobre os bgl
print('=-'*50)
print(print.__doc__) # outro tutotial
help(escreva)'''
somar(2, 3)
print('=-'*50)
a = 5
b = 7
print(f'a fora é {a}')
print('=-'*50)
print(f'b é global {b}')
print('=-'*50)
teste()
