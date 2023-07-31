'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
'''
import time
import sys
import os


print ('LISTA DE COMPRAS')
lista = []
menu = 'Adicionar item[+] | Remover ultimo item [-] | Apagar tudo [apagar] || Finalizar lista de Compras [fim]= '

while True:
    print('Produtos dentro da lista =')

    for item, produto in enumerate(lista):
        print(item,produto)
    
    resposta= input(menu)
    

    while resposta == '+':

        if resposta == '+':
            
            print('Inserindo itens...')
            adicionar=input('Escreva [sair] para Outras opcões ||Insira um item na lista: ')

        if adicionar == 'sair':
            os.system('cls')
            break

        elif adicionar != 'sair':
            
            lista.append(adicionar)
            print(lista)
            
            continue
                
                

    while resposta != '+':
   
            if resposta == '-':
                try:
                    lista.pop()
                    print('Removeu o ltimo produto')
                    print('Lista atualiazada =')

                    for item, produto in enumerate(lista):
                        print(item,produto)
                except:
                    os.system('cls')
                    print('Sem itens para Remover')
                    time.sleep(1)
                    
                    break

            #'''elif resposta == 'lista':
                
                #print('Lista de Compras =')
                #for item, produto in enumerate(lista):
                    #print(item,produto)
                    
                #break'''

            elif resposta == 'apagar':
                
                lista.clear()
                print('||LISTA VAZIA||')
                
                break

            else:        
                break

    while resposta == 'fim':
        os.system('cls')
        print('SUA LISTA DE COMPRAS = ')
        for item, produto in enumerate(lista):
            print(item,produto)
        
        time.sleep(10)
        sys.exit()
        
            

     


