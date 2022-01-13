# laços de repetição
for c in range(0, 5):  #aqui ele conta do 0-4
    print('Teste', end='')
print('\nFim1')
for c in range(1, 6):  # aqui ele conta do 1-5
    print(c, end='')
print('\nFim2')
for c in range(0, 10, 2):  # contou do 0-9 de 2 em 2
    print(c, end='')
print('\nFim3')
for c in range(10, -1, -1):  # COMEÇA do 10 e vai diminuindo 1
    print(c, end=' ')
print('\nFim4')
s = 0
for c in range(0, 3):
    n = int(input('Digite um número: '))
    s += n  # isso é a mesma coisa que ||| s = s + n ||| mas o python deixa escrever || s += n || s recebe ele +n
print('O somatório é: {}'.format(s))
f = input('Palavra: ')
par = int(len(f)/2)
for c in range(0, par):
    print(f[c])
