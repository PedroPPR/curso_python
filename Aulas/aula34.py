'''
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinaç igual
argumentos não nomeados recebem apenas o argumento (valor)

'''

def soma(x,y):
    #definição
    print(x+y)

soma(1,2)

def soma2(x,y):
    print(f'{x=} {y=}', '|', 'x + y =', x + y)

soma2(12,16)



