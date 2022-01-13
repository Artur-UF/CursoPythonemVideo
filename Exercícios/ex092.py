# contratação
from datetime import date
cont = {'nome': input('Nome: '),
        'idade': date.today().year - int(input('Data de nascimento: ')),
        'ctps': 0,
        'contratação': 0,
        'salário': 0,
        'aposentadoria': 0}
cont['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))
if cont['ctps'] != 0:
    cont['contratação'] = int(input('Ano de contratação: '))
    cont['salário'] = float(input('Salário: '))
    cont['aposentadoria'] = cont['idade'] + (35 - (date.today().year - cont['contratação']))
    for k, v in cont.items():
        print(f'{k} é: {v}')
else:
    del cont['contratação']
    del cont['salário']
    del cont['aposentadoria']
    for k, v in cont.items():
        print(f'{k} é: {v}')
