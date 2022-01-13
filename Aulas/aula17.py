import numpy as np
import math as mt
# Listas
from random import randint
teste = ['isso', 'é um', 'teste', 'de', 'listas']
print(f'1{teste}')
teste.append('fim')
print(f'2{teste}')
teste.insert(2, 'penetra')
print(f'3{teste}')
del teste[2]
print(f'4{teste}')
teste.pop(5)  # se não botar o índice ele remove o último
print(f'5{teste}')
teste.remove('isso')
print(f'6{teste}')
nums = [randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10), randint(0, 10)]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
for c, v in enumerate(nums):
    print(f'na posição {c} está o número {v}')
n = nums[:] # isso cria uma cópia, se não tivesse os [:] as duas estariam ligadas
comp = list((f'{mt.cos(x):.2f}', f'{mt.sin(x):.2f}')for x in np.linspace(0, 2*np.pi, num=12, endpoint=False))
print(np.linspace(0, 2*np.pi, num=4, endpoint=False))
print(comp)
