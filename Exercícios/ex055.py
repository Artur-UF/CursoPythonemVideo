# quem é o mais pesado e o mais leve?
controle = []
maior = [0]
menor = [0]
for c in range(0, 5):
    p = int(input('Peso: '))
    controle.append(p)
for c in range(0, 5):
    if controle[c] > maior[0]:
        maior[0] = controle[c]
menor[0] = maior[0]
for c in range(0, 5):
    if controle[c] < menor[0]:
        menor[0] = controle[c]
print('O maior peso é: {}'.format(maior))
print('O menor peso é: {}'.format(menor))
