frase = 'A marca fundamental do texto narrativo é a existência de um enredo, no qual são desenvolvidas as ações das personagens, marcadas pelo tempo e pelo espaço.' \
'Assim, a narração engloba o que chamamos de 5 elementos da narrativa:' \
'Enredo: designa a história da narrativa. Dependendo de como a trama é contada, ele é classificado em dois tipos: enredo linear (sequência cronológica) e enredo não linear (não possui uma sequência cronológica).'.lower()

print(frase.count('a'))

i=0
qts_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''


while i < len (frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue

    qtd_atual = frase.count(letra_atual)

    if qts_apareceu_mais_vezes < qtd_atual:
        qts_apareceu_mais_vezes= qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i+=1

print(f'A letra que apareceu mais vezes foi:"{letra_apareceu_mais_vezes}" -> apareceu {qts_apareceu_mais_vezes}x')




