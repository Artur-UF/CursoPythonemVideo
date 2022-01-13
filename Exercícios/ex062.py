# PA super otimizada
n = int(input('Digite o primeiro termo: '))
r = int(input('A razão: '))
c = 0
print('Os 10 primeiros termos foram:')
while c < 10:
    print(n, end=' ')
    c += 1
    n += r
cr = 0
i = 0
while i != '2':
    i = input('\nO que deseja fazer:\n[1] Ver mais x termos\n[2] Ou parar\n')
    if '1' in i:
        cr = int(input('Quantos termos ? '))
        c2 = 0
        while c2 < cr:
            print(n, end=' ')
            c2 += 1
            n += r
