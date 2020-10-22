# LISTAS

idade = 0

idades = [10, 27, 15, 18, 14, 23]

'''
print(type(idades))
print(type(idade))

print(f"Idades[2] = {idades[2]}")

print(f"Idades 0 a 2 = {idades[0:3]}")

print(f"Ultimo numero de Idades = {idades[-1]}")
'''

def permissao(idade):

    if idade >= 18:
        print(f'{idade} OK, Você está permitido !')
    else: 
        print(f'{idade} Tente novamente daqui alguns anos')


for idade in idades:
    permissao(idade)



'''
for idade in idades: 
    if idade >= 18:
        print(f'Você Já tem {idade} anos, Pode dirigir\n')

    else:
        print(f'Infelizmente com apenas {idade} anos você não Pode Dirigir\n')
'''
