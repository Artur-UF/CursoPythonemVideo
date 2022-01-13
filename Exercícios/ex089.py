# boletim
bd = []
al = []
nt = []
while True:
    no = input('Nome: ')
    al.append(no)
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    nt.append(n1)
    nt.append(n2)
    al.append(nt[:])
    bd.append(al[:])
    al.clear()
    nt.clear()
    r = input('Quer continuar? [S/N] ').strip().lower()[0]
    while r != 's' and r != 'n':
        r = input('Quer continuar? [S/N] ').strip().lower()[0]
    if r in 'n':
        break
print('=-'*20)
print(f'No.|  Nome    | Média')
print('-'*20)
for c in bd:
    print(f'{bd.index(c)+1:<3}|{c[0]:7}   | {(c[1][0]+c[1][1])/2:.2f} ')
print('=-'*20)
while True:
    r1 = input('Quer ver as notas de algum aluno? [S/N] ').strip().lower()[0]
    while r1 != 's' and r1 != 'n':
        r1 = input('Quer ver as notas de algum aluno? [S/N] ').strip().lower()[0]
    if r1 in 'n':
        break
    na = int(input('De qual aluno? '))
    print(f'As notas do aluno {bd[na-1][0]} são: {bd[na-1][1]}')
    print('-'*40)
