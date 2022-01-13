# Dicionários
teste = {'nome':'Artur', 'idade':20, 'peso':69}
print(teste['nome'])
# para adicionar algo:
teste['sexo'] = 'M'
print(teste['sexo'])
print(teste.keys())
print(teste.values())
print(teste.items())
for k, v in teste.items():
    print(f'O {k} é {v}')
teste1 = {'j1':7, 'j2':4, 'j3':8, 'j4':3}
print(sorted(teste1.keys()))
