#função input

print("Responda algumas perguntas")

nome = input(    'Qual o seu nome?')
print(f'O seu nome é {nome}.')

idade= input('Idade?')
print(f'Idade:{idade}')

int(idade)

ano_nascimento= input('Ano de nascimento?')
print(f'Ano Nascimento:{ano_nascimento}')

peso = input('Peso?')
print(f'Peso {peso}kg.')

int(peso)

altura=input(float('Altura?'))
print (f'Altura:{float(altura)}')

float(altura)

#calcule IMC

imc= peso/(altura*altura)

print(f'Pedro tem {idade} de idade, pesa {peso}kg, e seu imc atual é {imc}.P')
