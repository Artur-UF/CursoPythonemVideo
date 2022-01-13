nome = input('Digite o seu nome: ')
print('Olá', nome, ', seja bem vindo!')
print('Olá {:20}, seja bem vindo!'.format(nome)) #20 espaços
print('Olá {:>20}, seja bem vindo!'.format(nome))
print('Olá {:<20}, seja bem vindo!'.format(nome))
print('Olá {:^20}, seja bem vindo!'.format(nome))
print('Olá {:=^20}, seja bem vindo!'.format(nome)) #pode ser qualquer coisa que será copiada no lugar do espaço
