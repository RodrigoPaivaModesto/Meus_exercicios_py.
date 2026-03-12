#validador_senha_pro


def validador_senha_pro():
    print("--- CADASTRO DE SENHA ULTRA SEGURA ---")
    
    especiais = "!@#$%¨&*()_+-="

    while True:
        senha = input("\nCrie uma senha (mínimo 8 caracteres, 1 número e 1 especial): ")
        
        tamanho_ok = len(senha) >= 8
        tem_numero = False
        tem_especial = False

        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
            
            if not caractere.isalnum():
                tem_especial = True

        
        if tamanho_ok and tem_numero and tem_especial:
            print("Senha validada com sucesso!")
            break
        else:
            print("Senha insuficiente:")
            if not tamanho_ok:
                print("Mínimo de 8 caracteres.")
            if not tem_numero:
                print("Precisa de pelo menos um número.")
            if not tem_especial:
                print("Precisa de pelo menos um caractere especial (!@#$...).")


validador_senha_pro()
