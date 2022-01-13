from mod115.sistema import *
ark = 'cev.txt'
if not exark(ark):
    cark(ark)
op = ['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do programa']
while True:
    r = menu(op)
    if r == 1:
        escreva('Pessoas Cadastradas', tipo='-')
        readark(ark)
        lin('~')
    elif r == 2:
        escreva('Novo Cadastro')
        nom = input('Nome: ')
        idade = valid('Idade: ')
        writeark(ark, nom, idade)
    elif r == 3:
        print(f'Você escolheu a opção {r}')
        break
    else:
        print('\033[0;31mOpção não reconhecida.\033[m')
