# é número
def leiaint(n):
    num = input(n)
    while num.isnumeric() is False:
        print('\033[0::31mErro, isso não é um número inteiro.\033[m')
        num = input(n)
    inteiro = int(num)
    return inteiro


n = leiaint('Digite um número: ')
print(f'Você acabou de ler o número: {n}')
