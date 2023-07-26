'''
Escopo de funções em python
Escopo significa o local onde aquele código podde atingir.
existe o escopo global e local.
o escopo global é o escopo onde todo o código é alcançavel.
o escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
a palavra global faz uma variavel do escopo externo ser a mesma no escopo interno
'''

x= 1

def escopo():
    # global x
    x=10
    print(x)



escopo()