"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


try:
    a=input('Digite número Inteiro:')
    b=2
    inteiro_a = int(a)
    inteiro_b = int(b)
    modulo = (inteiro_a%inteiro_b)

    if modulo == 0:
        print(f'O número {a} é par')

    else:
        print(f'O número {a} é impar')
  

except:
    print('Não é um número inteiro')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora=input( 'que horas são?')
hora_int=int(hora)

if hora_int>=0  and hora_int<=11:
    print('Bom dia')

elif hora_int>=12 and hora_int<=17:
    print('boa tarde')

else:
    print('Boa noite')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"."""

nome=input('Qual seu nome?')

quantas_letras=len(nome)

if quantas_letras<=4:
    print('Nome pequeno')

elif quantas_letras>=5 and quantas_letras<=6:
    print('seu nome é normal')

else:
    print('Seu nome é grande')