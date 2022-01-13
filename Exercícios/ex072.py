# lendo números
nums = 'zero', 'um', 'dois', 'três', 'quetro', 'cinco',\
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',\
       'doze', 'treze', 'quatortze', 'quinze', 'dezesseis',\
       'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Número: '))
    if 0 <= n <= 20:
        break
print(f'O número por extenso é: {nums[n]}')
