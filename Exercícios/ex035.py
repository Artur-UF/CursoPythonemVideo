r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 >= r2 + r3 or r2 >= r1 + r3 or r3 >= r1 + r2:
    print('Não pode formar um triângulo.')
else:
    print('Pode formar um triângulo')
