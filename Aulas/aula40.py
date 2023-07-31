'''
ENUMERATe - enumera itaráveis (indices)

'''

lista = ['maria',  'helena', 'luiz']

lista.append('joão')

#lista_enumerada = enumerate(lista)

#for item in lista_enumerada:
    #print (item)

for indice, nome in enumerate(lista):
    print(indice, nome)

'''for item3 in enumerate(lista):
    for valor in item3:
        print(valor)'''
