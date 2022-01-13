# Erros e exceçoes
try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    di = n1/n2
except (ValueError, TypeError):
    print('Erro no dado informado.')
except ZeroDivisionError:
    print('Tentou dividir por zero seu espertalhão.')
except Exception as error:
    print(f'O erro foi: {error.__cause__}')
else:
    print(f'A divisão é: {di:.2f}')
finally:
    print('Obrigado, volte sempre!')