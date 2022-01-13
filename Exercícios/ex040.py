# Média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
me = (n1+n2)/2
if me < 5:
    print('\033[0:31mREPROVADO')
elif 5 <= me <= 6.9:
    print('\033[0:33mRECUPERAÇÃO')
else:
    print('\033[0:32mAPROVADO')
