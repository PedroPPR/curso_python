#

nome= 'Pedro'
altura= 1.72
peso=80
imc = peso/(altura*altura)

imc_int=int(imc)

print('Nome:',nome, '|','IMC:', imc_int)
print(nome, 'tem' , altura,'m', ', pesa', peso, 'kg e seu imc é', imc_int)

#f-strings
linha_1= f'{nome} tem {altura:,.3f}m de altura, pesa {peso}kg e seu imc é de {imc:,.2f}.'
print(linha_1)


