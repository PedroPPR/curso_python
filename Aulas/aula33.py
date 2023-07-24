'''
Introdução as funçoes (def) em python
Funções são trechos de códigos usados para replicar
determinadas ações ao longo do seu código
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, funções python retornam Nome (nada)
'''

def Print():
    print('Varias')
    print('varias2')
    print('Varias3')
    print('varias4')

Print()

def Numeros(x,y): #parametros
    print(x,y)

Numeros(1,2) #argumentos
Numeros(3,4)
Numeros(5,6)

def Soma(x,y):
    print((x+y))

Soma(1,2)

Soma(135454,51354356435645664)


def name(nome='Sem nome'):
    print(f'Olá, {nome}')
    print(f'{nome}, Seja bem vindo')

name(input('Qual seu nome?'))


    



