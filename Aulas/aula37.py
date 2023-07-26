'''
Listas em Python

Tipo list - mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamentos
Metodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete =lista [i] (CRUD)
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas


'''

#
#

string = 'ABCDE' # 5 caracteres (len)

lista = [123, True, 'Pedro ',1.2,[]]
print(lista)

print(lista[3])
print(lista[2].upper())
print(lista[4])

lista[2] = 'Maria'

lista2 = [10,20,30,40]

numero = lista2 [2]

print(numero)

lista2 [2] = 300

print(lista2)

del lista2[2]

print(lista2)

lista2.append(30)

print(lista2)

lista2.pop() ##remove o ultimo elemento

ultimo_valor=lista2.pop()

print(lista2, ultimo_valor)

print(lista)

lista.clear()

print(lista)

lista2.insert(0,5)
lista2.insert(0,'pedro')

print(lista2)

lista3 = [1,2,3,4,5,6,7,8,9,10]
lista4 = [11,12,13,45,8]

lista5 = lista3.extend(lista4)

print(lista5)

lista6 =lista3+lista4

print(lista6)