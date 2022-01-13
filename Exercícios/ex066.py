# soma dos números até o flag
soma = cont = 0
while True:
    n = int(input(('Digite um número: ')))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você escreveu {cont} números até atingir 999 e a soma deles é {soma}')
