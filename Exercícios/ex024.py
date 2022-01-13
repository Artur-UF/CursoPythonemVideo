ci = input('Cidade: ')
c = ci.lower().strip()
s = 'santo' in c[:5]
print('A cidade começa com Santo ?\n{}'.format(s))
