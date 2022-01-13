# Análise de triângulo
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 == r2 or r1 == r3 or r3 == r2:
    if r1 != r2 or r1 != r3 or r3 != r2:
        print('É um triângulo isóceles.')
    else:
        print('É um triângulo equilátero.')
elif r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Não forma triângulo.')
else:
    print('É um triângulo escaleno.')
