#operadores logicos
#and (e) |or (ou) |not (não)
#and todas as condiçoes precisam ser verdadeiras

'''entrada = input ('[E]ntrar ||| [S]air : ')
senha_digitada = input ('Senha: ')

senha_permitida= '123'



if entrada == 'E' and senha_digitada == senha_permitida:
    print ('Entrar')



elif entrada == 'E' and senha_digitada != senha_permitida:
    print(f'a senha {senha_digitada} estar errada')
    print('Saiu do sistema')

elif entrada == 'S':
    print('Saiu do sistema')

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

entrada = input ('[E]ntrar ||| [S]air : ')
senha_digitada = input ('Senha: ')

senha_permitida= '123'



if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print ('Entrar')



elif entrada == 'E' and senha_digitada != senha_permitida:
    print(f'a senha {senha_digitada} estar errada')
    print('Saiu do sistema')

elif entrada == 'S':
    print('Saiu do sistema')'''

''''''''''''''''''''''''''''''''''''''''''''''''

entrada = input ('[E]ntrar ||| [S]air : ')
senha_digitada = input ('Senha: ') 

senha_permitida= '123'



if entrada == 'E' or 'e' and senha_digitada == senha_permitida:
    print ('Entrar')

elif entrada == 'S' or 's':
    print('Saiu do sistema')


elif entrada == 'E' or 'e' and senha_digitada != senha_permitida:
    print(f'a senha {senha_digitada} estar errada')
    print('Saiu do sistema')


