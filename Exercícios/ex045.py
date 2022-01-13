# pedra papel tesoura
from random import choice
eu = input('Pedra, papel ou tesoura? ')
co = choice(['r', 'p', 's'])
if eu == 'pedra':
    if co == 'p':
        print('Você \033[0:31mperdeu\033[m!, o computador escolheu papel')
    elif co == 's':
        print('Você \033[0:32mganhou\033[m!, o computador escolheu tesoura')
    else:
        print('\033[0:33mEmpatou\033[m')
elif eu == 'papel':
    if co == 'r':
        print('Você \033[0:32mganhou\033[m!, o computador escolheu pedra')
    elif co == 's':
        print('Você \033[0:31mperdeu\033[m!, o computador escolheu tesoura')
    else:
        print('\033[0:33mEmpatou\033[m')
else:
    if co == 'p':
        print('Você \033[0:32mganhou\033[m!, o computador escolheu papel')
    elif co == 'r':
        print('Você \033[0:31mperdeu\033[m!, o computador escolheu pedra')
    else:
        print('\033[0:33mEmpatou\033[m')
