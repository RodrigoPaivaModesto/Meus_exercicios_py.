#lista de compras 

def lista_de_compras():
    compras = []

    print('MINHA LISTA DE COMPRAS')
    print("Digite o produto ou 'sair' para encerrar o programa\n")

    while True:
        item = input('Produto: ').strip().lower()

        if item == 'sair':
            break

        compras.append(item)
        print('produto adicionado a lista!')

    compras.sort()

    print('\nSua lista final organizada:')

    for produto in compras:
        print(f'{produto}')

lista_de_compras()