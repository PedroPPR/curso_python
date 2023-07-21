#Operadores in e not in
#strings são interáveis

#0 1 2 3 4 5
#Pedro
#-6 -5 -4 -3 -2 -1

'''nome =  'Pedro' or 'PEDRO'  

print(nome[2])
print(nome[-2])
print(nome[1])
print(nome[-1])
print(nome[-3])
print(nome[0])

print('a' in nome)

print('P' in nome)
print('e' in nome)
print('E' in nome)'''

nome = input('Digite um nome:')

encontrar = input('Digite uma letra:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}' )

else:
    print(f'{encontrar} não está em {nome}')