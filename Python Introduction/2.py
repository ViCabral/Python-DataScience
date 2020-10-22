
'''
nome = 'José'

def saudacao(nome_recebido):
    # nome = input('Qual seu nome?\n')
    print(f'Olá {nome}')

saudacao(nome) 

'''

idade = input('Declare sua Idade Terraqueo: ')
idade = int(idade)

def permissao(idade):

    if idade >= 18:
        print('OK, Você está permitido !')
    else: 
        print('Tente novamente daqui alguns anos')


permissao(idade)