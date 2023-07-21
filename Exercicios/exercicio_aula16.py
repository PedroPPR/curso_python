primeiro_valor= input('Digite um valor:')
segundo_valor= input('Digite outro valor:')

if primeiro_valor > segundo_valor:
    print('É maior')

    print(f'{primeiro_valor} é maior que {segundo_valor}')


elif primeiro_valor < segundo_valor:
    print('É menor')
    print(f'{primeiro_valor} é menor que {segundo_valor}')


elif primeiro_valor == segundo_valor:
    print('É igual')
    print(f'{primeiro_valor} é igual que {segundo_valor}')


'''
o print pode ser escrito como

    print(f'{primeiro_valor} é maior que {segundo_valor}')


'''