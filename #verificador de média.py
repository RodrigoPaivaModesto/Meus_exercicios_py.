#verificador de média


def calcular_média():
    N1 = float(input('digite a nota 1: '))
    N2 = float(input('digite a nota 2: '))
    N3 = float(input('digite a nota 3: '))

    média = (N1 + N2 + N3) / 3

    if média >= 7:
        print('Aprovado')

    elif média >= 5 and média < 7:
        print('Recuperação')

    else:
        print('Reprovado')


calcular_média()
