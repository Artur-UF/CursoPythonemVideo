# contador de adultos
from datetime import date
adulto = []
menor = []
ind = []
for c in range(0, 7):
    ano = int(input('Ano de nascimento: '))
    if date.today().year - ano > 18:
        adulto.append(c)
    elif date.today().year - ano < 18:
        menor.append(c)
    else:
        ind.append(c)
print('O número de adultos é: {}'.format(len(adulto)))
print('O número de menores de idade é: {}'.format(len(menor)))
print('O número de pessoas que fazem 18 anos esse ano é: {}'.format(len(ind)))
