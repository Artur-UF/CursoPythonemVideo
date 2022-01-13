# palíndromo
from math import ceil
f = input('Digite a frase: ').strip().split()
f1 = ''.join(f)
f2 = len(f1)
controle = []
if f2 % 2 == 0:
    n = int(f2/2)
    for c in range(0, n):
        if f1[c] == f1[-(c+1)]:
            controle.append(f1[c])
    if not controle:
        print('Não é palíndromo.')
    else:
        print('É palíndromo.')
else:
    n1 = ceil(f2/2)-1
    for c in range(0, n1):
        if f1[c] == f1[-(c+1)]:
            controle.append(f1[c])
    if not controle:
        print('Não é palíndromo.')
    else:
        print('É palíndromo.')
# esse script compara a priemira metade de uma str com a outra metade de trás pra frente
''' mas se você fizesse um fatiamento assim || f[::-1] || assim ele mostra do inicio ao fim de trás pra frente
 com isso o script podia ter umas 10 linhas'''