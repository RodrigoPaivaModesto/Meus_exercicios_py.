#validador de senhas 

def validador_senha():
    print('----Cadastro de senha----')

    while True:
        senha = input('Crie uma senha (mínimo de 8 caracteres e um número e um caractere especial): ')

        tamanho_ok = len(senha) >= 8

        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break

        if tamanho_ok and tem_numero:
            print('senha validada com sucesso')

        else:
            print('senha inválida')
            if not tamanho_ok:
                print('precisa ter pelo menos 8 caracteres')
            if not tem_numero:
                print('precisa ter pelo menos um número')

validador_senha()