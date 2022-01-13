# Brasileirâo
times = 'Bragantino', 'Athletico-PR', 'Palmeiras', 'Fortaleza',\
        'Bahia', 'Santos', 'Atlético-GO', 'Atlético-MG', 'Fluminense',\
        'Flamengo', 'Corinthians', 'Ceará', 'Internacional', 'Juventude',\
        'Sport', 'Cuiabá', 'São Paulo', 'Chapecoense', 'América-MG', 'Grêmio'
print(f'Os 5 primeiros colocados são:\n{times[:5]}')
print('=-'*50)
print(f'Os últimos 4 colocados:\n{times[-4:]}')
print('=-'*50)
print(f'Os times em ordem alfabética:\n{sorted(times)}')
print('=-'*50)
for c in range(0, 20):
    if times[c].lower() == 'chapecoense':
        print(f'A Chapecoense está na {c+1}° posição')
