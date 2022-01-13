# Loja
som = contmaior = maior = menor = cont = 0
nomm = ''
while True:
    nom = input('Nome do produto: ')
    pre = float(input('Preço: '))
    som += pre
    r = input('Deseja continuar? [S/N]: ')
    cont += 1
    if pre > 1000:
        contmaior += 1
    elif cont == 1:
        maior = menor = pre
    elif cont > 1:
        if pre > maior:
            maior = pre
        if pre < menor:
            menor = pre
            nomm = nom
    if r in 'Nn':
        break
print(f'O total da compra é: R${som}')
print(f'O número de itens com o preço maior que 1000 reais é: {contmaior}')
print(f'O item com o menor preço é: {nomm}')
