n = 0
c = 0
cr = 0
while n != 999:
    cr += 1
    c += n
    n = int(input('Digite um número: '))
print('Antes de digitar 999 você escreveu {} números e a soma deles é: {}'.format(cr, c))
