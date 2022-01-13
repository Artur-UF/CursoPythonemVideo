# Tabular
propre = 'Chocolate', 5.49, 'Batata', 3.99, 'Manteiga', 7.99,\
         'Brócolis', 2.99, 'Cenoura', 4.99, 'Bergamota', 2.49,\
         'Ovos', 7.49, 'Sorvete', 25.90, 'Açúcar', 8.59
print('='*30)
for c in range(0, len(propre), 2):
    print(f'{propre[c]:.<20}R${propre[c+1]:>5}')
print('='*30)
