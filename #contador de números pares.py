#contador de números pares

def contar_pares():
    soma = 0
    for numero in range(1, 51):
        if numero % 2 == 0:
            print(numero, end=',')

        soma += numero

    print('\n' + '-' * 20)

    #soma = soma + numero

    print(f'A soma de todos os pares é: {soma}')


contar_pares()