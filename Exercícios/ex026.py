n = input('Nome: ')
print('A letra a aparece quantas vezes ?\n{}'.format(n.lower().strip().count('a')))
print('Onde aparece o primeiro a ?\n{}'.format(n.lower().strip().find('a')))
print('Onde está o último a ?\n{}'.format(n.lower().strip().rfind('a')))
