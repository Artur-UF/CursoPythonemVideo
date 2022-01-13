# ordem
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = input('Deseja comtinuar? [S/N] ').lower().strip()[0]
    while r != 's' and r != 'n':
        r = input('Deseja comtinuar? [S/N] ').lower().strip()[0]
    if r in 'n':
        break
print(f'A sequência de números inversa é {sorted(lista, reverse=True)}')
print(f'Você digitou {len(lista)} números')
print('O 5 está na lista'if 5 in lista else'O 5 não está na lista')
