# Caixa eletrônico
n = int(input('Qual valor você deseja sacar? :R$'))
c50 = n//50
c20 = (n-(c50*50))//20
c10 = (n-((c50*50)+(c20*20)))//10
c1 = n-((c50*50)+(c20*20)+(c10*10))
if c50 > 0:
    print(f'Cédulas de 50: {c50}')
if c20 > 0:
    print(f'Cédulas de 20: {c20}')
if c10 > 0:
    print(f'Cédulas de 10: {c10}')
if c1 > 0:
    print(f'Cédulas de 1: {c1}')
