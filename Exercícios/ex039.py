# Alistamento
from datetime import date
n = int(input('Qual o seu ano de nascimento? '))
i = date.today().year - n
if i < 18:
    print('Faltam {} anos para você se apresentar.'.format(18-i) )
elif i > 18:
    print('Você está atrasado {} anos para o alistamento.'.format(i-18))
else:
    print('Você deve se apresentar esse ano.')
