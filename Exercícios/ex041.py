# Faixas etárias
from datetime import date
n = int(input('Ano de nascimento: '))
i = date.today().year - n
print('Sua idade é: {}'.format(i))
if i <= 9:
    print('É mirim.')
elif i > 9 and i <= 14:
    print('É infantil.')
elif i > 14 and i <= 19:
    print('É júnior.')
elif i > 19 and i <= 20:
    print('É sênior.')
else:
    print('É master.')
