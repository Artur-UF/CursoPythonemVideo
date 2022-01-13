# Criação da tupla
val = int(input('Digite um valor: ')), int(input('Digite um valor: ')),\
      int(input('Digite um valor: ')), int(input('Digite um valor: '))
cont1 = 0
valp = []
pos = 0
for c in range(0, 4):
    if val[c] == 9:
        cont1 += 1
    if val[c] % 2 == 0:
        valp.append(val[c])
print(f'Os valores digitados foram: {val}')
print(f'O 9 aparece {cont1} vezes')  # podia usar val.count(9)
print(f'O 3 aparece na {(val.index(3))+1}° posição'if 3 in val else 'O 3 não aparece')
print(f'Os valores pares são: {valp}')
