# fake sort
lista = [int(input('Digite um valor: '))]
print('Primeiro número adicionado.')
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if n > max(lista):
        lista.append(n)
        print('Número adicionado na última posição')
    elif n <= min(lista):
        lista.insert(0, n)
        print('Número adicionado na posição 1')
    else:
        for v in range(0, len(lista)):
            if n < lista[v]:
                lista.insert(v, n)
                print(f'O número foi adicionado na posição {v+1}')
                break
print(lista)