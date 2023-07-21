#input

'''
numero_1= int(input('DIGITE UM NÚMERO')) #gera erro int
numero_2= int(input('DIGITE OUTRO NÚMERO'))

print(f'A soma dos números é: {numero_1+numero_2}')
'''

numero_1 = input('DIGITE UM NÚMERO: ') #gera erro int
numero_2 = input('DIGITE OUTRO NÚMERO: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1+int_numero_2}')