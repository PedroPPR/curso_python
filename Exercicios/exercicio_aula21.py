#Exercicio
'''
PEÇA AO USUARIO PARA DIGITAR SEU NOME
PEÇA PARA DIGITAR DIA/MES/ANO
PEÇA PARA DIGITAR PROFISSÃO

    EXIBIR:
    NOME
    NOME INVERTIDO
    NOME CONTEM ESPAÇOS OU NÃO
    NOME CONTÉM QUANTAS LETRAS
    QUAL PRIMEIRA LETRA?
    QUAL A ULTIMA LETRA?

SE NADA FOR DIGITADO APARECER UMA MENSAGEM

'''

nome = input('Qual é seu nome?')
data_nascimento = input('DIA/MÊS/ANO de nascimento:')
job = input('Qual sua profisão?')
letra_nome = len(nome)




if nome:
    print(f'Nome: {nome}')
    print(f'Nome invertido:{nome[::-1]}')
   
    if ' ' in nome:
        print(f'Nome {nome} contem espaços.')
    else:
        print('Não contém espaços')
    print(f'Seu nome tem:{len(nome)} letras')
    print(f'A primeira letra do nome é: {nome[0]}')
    #print(nome[len(nome)])
    print(f'A ultima letra do nome é : {nome[-1]}')

    
elif not nome:
    print('Você não inserio o nome')

if data_nascimento:
    print(f'Nascimento: {data_nascimento}')
elif not data_nascimento:
    print('Você não inserio a data de nascimento')

if job:
    print(f'Profissão:{job}')
elif not job:
    print('Você não insterio seu trabalho')





