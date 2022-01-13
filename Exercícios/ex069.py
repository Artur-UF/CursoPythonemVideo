# cadastro || [1] pessoas +18 || [2] quantos homens || [3] mulheres -20 ||
pm = ho = mm = 0
while True:
    print('-='*10)
    i = int(input('Idade: '))
    s = input('Sexo [F/M]: ')
    while s not in 'FfMm':
        s = input('Sexo [F/M]: ')
    if i > 18:
        pm += 1
    if s in 'mM':
        ho += 1
    if s in 'Ff' and i < 20:
        mm += 1
    co = input('Quer continuar ? [S/N] ')
    while co not in 'SsNn':
        co = input('Quer continuar ? [S/N] ')
    if co in 'Nn':
        break
print(f'O número de maiores de idade foram: {pm}\nO número de homens: {ho}\nO número de mulheres -20: {mm}')
