# 1)média de idade 2) homem mais velho 3) quantas munlheres com mais de 20 anos
p1 = 0
p2 = [0]
p21 = [0]
p3 = 0
print('Feminino = f\nMasculino = m')
for c in range(0, 4):
    print('='*10)
    n = input('Nome: ')
    i = int(input('Idade: '))
    s = input('Sexo: ')
    p1 += i
    if 'f' in s and i < 20:
        p3 += 1
    elif 'm' in s and i > p2[0]:
        p2[0] = i
        p21[0] = n
print('A média das idades é: {}'.format(p1/4))
print('O homem mais velho é o: {}'.format(p21[0]))
print('O número de mulheres com menos de 20 anos é: {}'.format(p3))
