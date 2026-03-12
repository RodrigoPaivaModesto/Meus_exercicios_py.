#sistema de cadastro

def cadastrar_usuario():
    usuario = {}

    usuario['nome'] = input('digite seu nome: ')
    usuario['idade'] = int(input('digite sua idade: '))
    usuario['e-mail'] = input('digite seu e-mail: ')

    print('\n----usuario cadastrado com sucesso----')

    print(f'Seja bem vindo, {usuario['nome']}! envimos um código de confirmação para {usuario['e-mail']}.')

cadastrar_usuario()