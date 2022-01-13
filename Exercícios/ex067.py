# tabuada negativofóbica
while True:
    n = int(input('Quer ver a tabuada de qual número ? '))
    if n < 0:
        break
    print(f'A tabuada de {n} é:')
    cont = 0
    while cont < 10:
        cont += 1
        print(f'{n} x {cont:2} = {n*cont}')
print('Acabou.')
