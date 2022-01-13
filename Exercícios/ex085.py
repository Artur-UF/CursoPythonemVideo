# pares e ímpares
nums = [[], []]
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
print(f'Os números pares foram: {sorted(nums[0])}\nOs números ímpares foram: {sorted(nums[1])}')
