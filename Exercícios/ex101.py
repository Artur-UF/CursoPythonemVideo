# voto
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade}: Não pode votar.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}: O voto é opcional.'
    else:
        return f'Com {idade}: O voto é obrigatório'


y = int(input('Em que ano você nasceu? '))
print(voto(y))
