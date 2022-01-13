# calculadora
op = ''
while op != '5':
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    op = input('Escolha a operação desejada:\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Novos Números\n[5] Fechar calculadora\n')
    if op == '1':
        print('{:2} + {:2} = {:2}'.format(n1, n2, (n1+n2)))
    elif op == '2':
        print('{:2} - {:2} = {}'.format(n1, n2, (n1-n2)))
    elif op == '3':
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
print('Calculadora fechada.')