# cadastro MAIS UMA VEZ
cad = []
so = 0
while True:
    n = input('Nome: ')
    i = int(input('Idade: '))
    so += i
    s = input('Sexo [M/F]: ').strip().lower()[0]
    pe = {'Nome': n, 'Idade': i, 'Sexo': s}
    cad.append(pe)
    r = input('Quer continuar? [S/N] ').strip().lower()[0]
    while r != 's' and r != 'n':
        r = input('Quer continuar? [S/N] ').strip().lower()[0]
    if r in 'n':
        break
print(f'O grupo tem {len(cad)} pessoas')
print(f'A média das idades é {so/len(cad)}')
print('As mulheres cadasstradas foram: ', end='')
for c in cad:
    if c['Sexo'] in 'f':
        print(c['Nome'], end=' ')
print('\nAs pessoas com  a idade acima da média do grupo são: ')
for c in cad:
    if c['Idade'] > (so/len(cad)):
        print(f'Nome = {c["Nome"]} ; Idade = {c["Idade"]} ; Sexo = {c["Sexo"]}')