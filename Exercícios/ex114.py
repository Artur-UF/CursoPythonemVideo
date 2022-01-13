from urllib import request
try:
    request.urlopen('http://pudim.com.br/')
except:
    print(f'\033[0;31mO site não está disponível.\033[m')
else:
    print(f'\033[0;32mO site está disponível.\033[m')
