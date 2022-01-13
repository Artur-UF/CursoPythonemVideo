# notas
def notas(*nts, sit=False):
    """
    => Vai receber várias notas e identificar sua média, o maior e menor valor
    :param nts: declare as notas
    :param sit: naturalmente False mas se colocar True diz a situação do aluno
    :return: retorna um dicionário com todas as informações
    """
    aluno = {'total': len(nts),
             'maior': max(nts),
             'menor': min(nts),
             'média': sum(nts)/len(nts)}
    if sit:
        if aluno['média'] < 6:
            aluno['situação'] = 'RUIM'
        if 6 <= aluno['média'] < 7:
            aluno['situação'] = 'REGULAR'
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
    return aluno


n = notas(5.6,  8.6, 6.5, 9)
print(n)
