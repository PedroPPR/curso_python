'''
Inteirando strings com while
'''
'''
nome = 'Pedro'

print(nome[-2])

tamanho_nome = len(nome)

print(tamanho_nome)

#nova_string += '*P*E*D*R*O'

'''


nome = input('Digite seu nome:')
separador = input('Digite um separador:')

indice = 0 
novo_nome = ''
while indice <len(nome):
    letra = nome[indice]
    novo_nome += f'{separador}{letra}'
    indice += 1

novo_nome += f'{separador}'

print(novo_nome)