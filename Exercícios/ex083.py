# validando expressões
cole = []
cold = []
ex = input('Digite a expressão: ')
for c in ex:
    if c in '(':
        cole.append(c)
    if c in ')':
        cold.append(c)
if len(cole) == len(cold):
    print('Essa expreção é válida.')
else:
    print('Essa expressão não é válida.')
print(f'Primeira lista: {cole}\nSegunda lista: {cold}')
# se dependesse da ordem dos parenteses vc teria que condicionar a adição de um parenteses com a existência do seu par