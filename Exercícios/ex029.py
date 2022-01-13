v = float(input('Velocidade lida: '))
if v >= 80:
    print('Se fudeu, multa de {} pila seu malandro!'.format((v-80)*7))
else:
    print('Foda-se')
