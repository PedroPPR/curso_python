'''CALCULADORA COM WHILE'''
print('CALCULADORA')


while True:
    
    
    while True:
        a= input('Digite A:')
        
        try:
                int_a = int(a)
                break
                
        except:
                print('A não é número inteiro')
                
    while True:
        b=input('Digite B:')

        try:
                int_b = int(b)
                break
                
        except:
                print('A não é número inteiro')
                
    

    print(f'A={a} e B={b}')

    operacao = input('Insira qual operação:')


    soma = int_a + int_b
    subtracao = int_b - int_b
    multiplicacao = int_a * int_b
    divisao = int_b / int_b

    if operacao == '+':
            print(f'{a}{operacao}{b}={soma}')
            continuar = input('[C]continuar//[S]sair:')
            continuar= continuar.lower()
            if continuar == 'c':
                print('Continuar')
            else:
                print('Você saiu...')
                break    
            
    elif operacao == '-':
            print(f'{a}{operacao}{b}={subtracao}')
            continuar = input('[C]continuar//[S]sair:')
            continuar= continuar.lower()
            if continuar == 'c':
                print('Continuar')
            else:
                print('Você saiu...')
                break  

    elif operacao == '*':
            print(f'{a}{operacao}{b}={multiplicacao}')
            continuar = input('[C]continuar//[S]sair:')
            continuar= continuar.lower()
            if continuar == 'c':
                print('Continuar')
            else:
                print('Você saiu...')
                break  

    elif operacao == '/':
            print(f'{a}{operacao}{b}={divisao}')
            continuar = input('[C]continuar//[S]sair:')
            continuar= continuar.lower()
            if continuar == 'c':
                print('Continuar')
            else:
                print('Você saiu...')
                break  

    else:
        print('Check se você digitou corretamente a operação')
        continuar = input('[C]continuar//[S]sair:')
        continuar= continuar.lower()
        if continuar == 'c':
                print('Continuar')
        else:
            print('Você saiu...')
            break  
    
