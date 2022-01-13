c = 0
r = 0
s = 0
n = 0
coma = 0
come = 0
while r != 2:
    c += 1
    r = int(input('Se quiser:\n[1]Digite um número\n[2]Saia do programa\n'))
    if r == 1:
        n = int(input('Número: '))
        s += n
        if c == 1:
            coma = come = n
        else:
            if n > coma:
                coma = n
            if n < come:
                come = n
print('A média dos números digitados é: {:.2f}'.format(s/(c-1)))
print('O maior número é: {}'.format(coma))
print('O menor número é: {}'.format(come))
