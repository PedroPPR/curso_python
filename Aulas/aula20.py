#interpolação básica de strings
#s - string
#d e i - int
#f - float
# x e X - Hexadecimal (ABCDEF0123456789)

print('Exemplo 1')

nome = 'Pedro'

preco = 1000.6584562

variavel = '%s o preço total foi R$%f' % (nome, preco)

print(variavel)



print('Exemplo 2')

nome = 'Pedro'

preco = 1000.6584562

variavel = '%s o preço total foi R$%.2f' % (nome, preco)

print(variavel)

print('Exemplo 3')

nome = 'Pedro'

preco = 1000.6584562

variavel = f'{nome} o preço total foi R${preco}'

print(variavel)

print('Exemplo 4')

nome = 'Pedro'

preco = 1000.6584562

variavel = f'{nome} o preço total foi R${preco: .2f}'

print(variavel)



"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

