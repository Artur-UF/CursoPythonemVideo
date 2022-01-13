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
