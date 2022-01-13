# maior e menor DE NOVO
lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print(f'A lista é: {lista}')
print(f'O maior número dela é {max(lista)} e está na posição', end=' ')
for p, n in enumerate(lista):
    if n == max(lista):
        print(f'{p+1}...', end=' ')
print(f'\nO menor número dela é {min(lista)} e está na posição', end=' ')
for p, n in enumerate(lista):
    if n == min(lista):
        print(f'{p+1}...', end=' ')
