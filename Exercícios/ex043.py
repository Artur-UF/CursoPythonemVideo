# cálculo IMC
p = float(input('Qual o seu peso em kg? '))
a = float(input('Qual a sua altura em metros? '))
imc = p/(a**2)
print('O seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você tem sobrepeso.')
elif 30 <= imc < 40:
    print('Você é obeso.')
else:
    print('Você tem obesidade mórbida.')
