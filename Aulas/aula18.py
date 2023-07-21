#Operador Lógico "not"
#usado para inverter expressões
#not True = False
#not False = True

'''
senha = input('Senha:')

if senha == '123':
    print('Entrou')

else :   
    print ('senha incorreta.')
    '''

senha = input('Senha:')



if not senha:
    print('voce não digitou')

elif senha != '123':
    print( 'senha incorreta.')


print(not True) #False
print(not False) #True



