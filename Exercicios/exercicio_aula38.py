'''
Exercicio
Exiba os indices da lista
Pedro
paulo
rego

'''

lista = ['Pedro','Paulo', 'Rego']

indices = range(len(lista))


for nome in lista:
    print(nome, indices)

for indice in indices:
    print(indice, lista[indice] )