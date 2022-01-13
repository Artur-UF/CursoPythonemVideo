# separando par e impar
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja continuar? [S/N]').strip().lower()[0]
    while r != 's' and r != 'n':
        r = input('Deseja continuar? [S/N]').strip().lower()[0]
    if r in 'n':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa: {lista}')
print(f'A lista com os pares: {par}')
print(f'A lista com os ímpares: {impar}')