# Pagamento
pr = float(input('Qual o valor? '))
cp = input('Quer pagar à vista ou parcelado? ')
if 'vista' in cp:
    ma = input('Vai ser no dinheiro/cheque ou no carão? ')
    if 'dinheiro' in  ma or 'cheque' in ma:
        print('O valor a pagar será de: R${}'.format(pr*0.9))
    else:
        print('O valor a pagar será: R${}'.format(pr*0.95))
elif 'parcelado' in cp:
    v = int(input('Em quantas vezes? '))
    if v <= 2:
        print('O valor a pagar será: R${}'.format(pr))
    else:
        print('O valor a pagar será de: R${}'.format(pr*1.2))
