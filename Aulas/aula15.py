# interrompendo o while
contador = 0
while contador <= 10:
    print(contador, end=' ')
    contador += 1
print('\nOu')
cont = 0
while True:
    print(cont, end=' ')
    cont += 1
    if cont == 11:  # essa condição com o "break" interrompe o while
        break
print(f'\nDescobri agora que posso formatar a str fazendo isso {cont}, pse né.')  # todas as formataçoes com {:.f} e tudo isso funciona ainda
print(f'Teste pra ver se o comentário funciona: {4/3:.2f}')
print('\nAcabou')


'''Escrever "continue" em um while True leva o fluxo do código de volta ao início'''