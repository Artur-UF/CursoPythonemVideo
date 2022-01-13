# fatiamento, análise de str
f = 'Artur Uhlik Frohlich'
print(f[:4])
print(f[15:])
print(f[8:13])
print(f[:14:2])
print(len(f))
print(f.count('m'))
print(f.find('Artur'))
print(f.split())
print('Tentando {:.<20}'.format(f))
f1 = f.split()
f2 = '-'.join(f1)
print(f2)

