'''
repetições
while (enquanto)
executa enquanto uma condição for verdadeira
'''

contador = 0

while contador <=1000:
    contador += 1
   

    
    if contador >=10 and contador <=500:
       print('não mostrar')
       continue

    print(contador)

    if contador == 1000:
     break