import math
n = float(input('Ângulo: '))
a = math.radians(n)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))
