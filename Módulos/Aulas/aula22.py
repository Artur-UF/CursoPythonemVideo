# fazendo módulos
import módulo
from util import strs
strs.escreva('Aula de módulos')
num = int(input('Digite um número: '))
print(f'O seu fatorial: {módulo.fatorial(num)}')
print(f'A sua raiz quadrada é: {módulo.raiz(num, rad=3):.3f}')
