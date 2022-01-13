# empréstimo para casa
vc = float(input('Qual o valor da casa? '))
sa = float(input('Qual o seu salário? '))
te = float(input('Em quantos anos quer pagar? '))
pr = vc/(te*12)
print('O valor da prestação é de {:.2f} reais'.format(pr))
if pr <= (sa*0.3):
    print('Seu empréstimo é possível!')
else:
    print('Seu salário é insuficiente :(')
