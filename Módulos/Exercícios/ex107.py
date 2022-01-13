# valores
from Módulos import moeda
p = float(input('Diga o preço: R$'))
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} temos: {moeda.aumentar(p, 10)}')
print(f'Diminuindo 20% de {p} temos: {moeda.diminuir(p, 20)}')
