def din(val):
    if '.' not in val:
        while val.isnumeric() is False:
            if ',' in val:
                num = val.replace(',', '.')
                return num
            else:
                print('\033[1;31mErro, numeral não identificado!\033[m')
                val = input('Digite um valor: ')
        return val
    else:
        return val
