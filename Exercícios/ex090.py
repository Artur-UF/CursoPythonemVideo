# situação do aluno
al = {'Nome':input('Nome: '), 'Média':float(input('Qual a média? '))}
for k, v in al.items():
    print(f'{k} é {v}')
if al['Média'] >= 6:
    print('\033[0::32mAprovado')
else:
    print('\033[0::31mReprovado')