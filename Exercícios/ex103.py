# jogador
def ficha(nom='<desconhecido>', gols='0'):
    if nom == '' and gols == '':
        return f'O jogador <desconhecido> fez 0 gol(s) no campeonato.'
    elif gols == '':
        return f'O jogador {nom} fez 0 gol(s) no campeonato.'
    elif nom == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nom} fez {gols} gol(s) no campeonato.'


print(ficha(input('Nome: '), input('Número de gols: ')))
