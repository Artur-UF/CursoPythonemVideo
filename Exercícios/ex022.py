a = input('Nome comleto: ')
n = a.strip()
print(n.upper())
print(n.lower())
di = n.split()
print(len(''.join(di)))  # juntar a lista 'di' com oq está entre aspas ( nada )
print(n.find(' '))  # achar o primeiro espaço
print(n[-8:])  # números negativos fazem o fatiamento reverso
di[-1:] = ['Silva']  # aqui eu substitui o último termo da lista gerada pela str entre []
print(' '.join(di))
