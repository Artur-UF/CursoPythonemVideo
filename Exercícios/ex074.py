# tupla aleatória
from random import randint
nums = randint(0, 10), randint(0, 10),\
       randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os números gerados foram: {nums}')
maior = menor = 0
for c in range(1, 6):
    if c == 1:
        maior = menor = nums[c-1]
    else:
        if nums[c-1] > maior:
            maior = nums[c-1]
        if nums[c-1] < menor:
            menor = nums[c-1]
print(f'O maior é {maior} e o menor é {menor}')
print(f'O maior {max(nums)} e o menor {min(nums)}')
