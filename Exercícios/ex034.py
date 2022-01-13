s = int(input('Salário: '))
if s > 1250:
    print('Seu novo salário é: {:.2f}'.format(s*1.1))
else:
    print('Seu novo salário é: {:.2f}'.format(s*1.15))
