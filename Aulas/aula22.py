# módulos
def fatorial(no):
    f = 1
    for c in range(1, no+1):
        f *= c
    return f


num = int(input('Digite um número: '))
fat = fatorial(num)
print(f'O fatorial de {num} é: {fat}')