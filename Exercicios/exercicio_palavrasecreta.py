'''
Faça um jogo para o usuario adivinhar qual a palavra secreta

- Vc vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra.
- quando o usuario digitar uma letra, vc vai conferir se a letra digitada está na palavra secreta.
    - se a letra digitada estiver na palavra secreta, exiba a letra;
    - se a letra digitada não estiver na palavra secreta, exiba *.
    faça contagem de tentativas para o seu usuario.
'''
print('-' * 23)

print('Jogo da Palavra Secreta')

print('-' * 23)

print('-' * 23)

print('Depois de 10 letras o jogo termina.')

print('-' * 23)

palavra_secreta = ('helicoptero')

tem_letra = True

contador = 0




while tem_letra:
    letra= input('Digite uma letra: ')

    procurar = palavra_secreta.count(letra)
    contador = contador + 1

    if procurar == 0:
        print(f'A letra |{letra}| não existe na palavra secreta.')
        print(contador)
        if contador >=10:
            print(f'Você já tentou 10 vezes e não acertou. A palavra secreta é |{palavra_secreta}|.')
            break

                
    elif procurar >=1:
                
        print(f'A letra|{letra}| existe na palavra secreta {procurar} x.')
        print(contador)
        if contador >=10:
            print(f'Você já tentou 10 vezes. A palavra secreta é |{palavra_secreta}|.')
            break

    
'''
_______________________________________________________________________________________________________________________________________________
Código do Curso:
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0


'''
    

        
        

           
    
            
        

   

    



