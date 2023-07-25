----------------------------------------------------------------------------------------------------
Erro
tentando aprender como faz um contador usando def 

----------------------------------------------------------------------------------------------------

'''def contador(x,y,z):'''

'''x=input('Inicio=')
y=input('Fim=')
z=input('Step=')'''


'''x=(1)
y=(10)
z=(1)

contagem = range([x],[y],[z])
              
for n in contagem:
    print(n)'''

'''contador()'''
'''inicio= input('Inicio=')
fim= input('fim=')
step= input('step=')

inicio_int = int(inicio)
fim_int= int(fim)
step_int= int(step)

x = range((inicio_int), (fim_int), (step_int))
for n in x:
  print(n, end='|')'''

def inserir(inicio, fim, step):
    inicio= input('Inicio=')
    fim= input('fim=')
    step= input('step=')
    

def inteiro(inicio_int, fim_int, step_int):
    inicio_int = int(inicio)
    fim_int= int(fim)
    step_int= int(step)

def operacao():
    x = range((inicio_int), (fim_int), (step_int))
    for n in x:
        print(n, end='|')

def espaco():
    print(('-'* 50))

inserir()

inteiro()

operacao()

espaco()

   
