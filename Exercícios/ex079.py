# cadastro
lista = []
while True:
    n = int(input('Digite um número: '))
    if n in lista:
        while n in lista:
            n = int(input('Valor já adicionado, digite outro número: '))
    if n not in lista:
        lista.append(n)
    r = input('Quer continuar ? [S/N] ').strip().lower()[0]
    while r != 's' and r != 'n':
        r = input('Quer continuar ? [S/N] ')
    if r in 'Nn':
        break
print(f'Os valores são {sorted(lista)}')
lista.sort()
print(f'Os valores são {lista}')
