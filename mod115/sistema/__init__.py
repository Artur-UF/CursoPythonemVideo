def lin(tipo='=', tam=30):
    return print(tipo*tam)


def escreva(msg, tipo='='):
    lin(tipo=tipo)
    print(f'{msg:^30}')
    lin(tipo=tipo)


def valid(msg):
    while True:
        num = input(msg).strip()
        try:
            n = int(num)
        except:
            print(f'\033[0;31mErro, opção < \033[m{num}\033[0;31m > não identificada >>> Tente novamente.\033[m')
            continue
        else:
            return n


def menu(lista):
    escreva('Menu Principal')
    for c in lista:
        print(f'\033[0;33m{lista.index(c)+1}\033[m - \033[0;34m{c}\033[m')
    lin()
    r = valid('\033[0;33mSua opção:\033[m ')
    return r


def exark(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def cark(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Não consegui criar o arquivo.')
    else:
        pass


def readark(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Deu brete.')
    else:
        print(f'Nome{"Idade":>25}')
        lin('~')
        print(a.read())
    finally:
        a.close()


def writeark(ark, nome='<desconhecido>', idade=0):
    try:
        a = open(ark, 'at')
    except:
        print('Deu brete ao abrir.')
    else:
        try:
            a.write(f'{nome:<24}{idade}\n')
        except Exception as erro:
            print(f'Deu esse brete {erro}.')
        else:
            print('Novo cadastro realizado')
            a.close()
