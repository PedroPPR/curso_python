#try and except
#try tenta executar o código
#except  ocorreu algum erro ao tentar executar


numero_str = (input('vou dobrar o numero que você colocar:'))

try:
    print('STR:',numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float*2:.2f}')


except:
    print('isso não é um número')





