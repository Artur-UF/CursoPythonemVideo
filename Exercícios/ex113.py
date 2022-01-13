# validação de números
def leiaint(n):
    num = input(n)
    while num.isnumeric() is False:
        print('\033[0::31mErro, isso não é um número inteiro.\033[m')
        num = input(n)
    inteiro = int(num)
    return inteiro


def leiafloat(n):
    num = input(n).replace(',', '.').strip()
    while True:
        try:
            t1 = float(num)
        except Exception as erro:
            print(f'\033[0::31mErro do tipo <{erro.__doc__}>, digite um número fracionário válido\033[m')
            num = input('\033[0;34mTenta de novo:\033[m ').replace(',', '.').strip()
        else:
            return t1


n = leiaint('Digite um número inteiro: ')
print(n)
dec = leiafloat('Digite um número fracionário: ')
print(dec)
'''while num.isnumeric() is False:
        print('\033[0::31mErro, isso não é um número inteiro.\033[m')
        num = input(n)
    decimal = float(num)'''