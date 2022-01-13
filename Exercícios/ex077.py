# Achando vogais
pal = 'ola', 'meu', 'nome', 'artur', 'estou',\
      'aprendendo', 'python', 'bem', 'legal', 'tchau'
'''for c in range(0, len(pal)):
    print(f'\nA palavra {pal[c]} tem as vogais:', end=' ')
    n = pal[c]
    for c1 in range(0, len(n)):
        if n[c1] in 'aeiou':
            print(n[c1], end=' ')'''
for c in pal:
    print(f'\nA palavra {c} tem as vogais:', end=' ')
    for l in c:
        if l in 'aeiou':
            print(l, end=' ')

