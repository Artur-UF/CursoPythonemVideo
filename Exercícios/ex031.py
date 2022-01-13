d = float(input('Distância: '))
if d > 200:
    print('Sua passsagem custa: {:.2f}'.format(d*0.45))
else:
    print('Sua passagem custa: {:.2f}'.format(d*0.5))
