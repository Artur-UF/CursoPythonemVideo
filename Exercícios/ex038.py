# qual valor é maior?
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('{} é o maior'.format(n1))
elif n2 > n1:
    print('{} é o maior'.format(n2))
else:
    print('Eles são iguais!')
