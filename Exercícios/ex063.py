# fibonacci
r = int(input('Quantos termos da sequência de Fibonacci você quer ? '))
c = 0
n = 1
n1 = 0
n2 = 0
print(0, end=' ')
while c < r-1:
    c += 1
    print(n, end=' ')
    n2 = n
    n += n1
    n1 = n2
