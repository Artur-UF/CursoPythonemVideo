from Módulos import moeda
p = float(input('Diga o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(9)} temos: {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 20% de {moeda.moeda(p)} temos: {moeda.diminuir(p, 20, True)}')
