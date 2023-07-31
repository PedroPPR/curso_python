'''
Introdução ao desempacotamento + tuples (tuplas)

'''

nomes = ['Pedro', 'Paulo', 'Cibelle']

nome1, nome2, nome3 = nomes

print(nome2)

print(nome1, nome3)

nome1, *resto = ['mesaque', 'osmelia','sophia']

print(resto)
print(nome1)

nome5, *_ =['fulana', 'hercules', 'pupuca']

print(nome5, _)

#___________________________________________________________________________________________________________

#tipo tupla - Uma lista imutável

nomes = 'Melo', 'Rego' #não colocar [] cria uma tuple

print(nomes)

print(nomes[0])

nomes = ['luiz', 'fernando']

nomes = tuple(nomes)

print (nomes [-1])
print(nomes)

nomes = list(nomes)

print(nomes)

