#simulador de caixa eletrônico

def caixa_eletronico():
    print('=' * 20)
    print('{:^20}'.format('banco R-Python'))
    print('=' * 20)


    saque = int(input('Qual valor deseja sacar ?: R$ '))
    total = saque 
    cedula = 100
    total_cedulas = 0

    while True:
        if total >= cedula:
            total -= cedula
            total_cedulas += 1

        else:
            if total_cedulas > 0:
                print(f'total de {total_cedulas} cédulas de R$ {cedula}')

            if cedula == 100:
                cedula = 50
            elif cedula == 50:
                cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 5
            elif cedula == 5:
                cedula = 2

            total_cedulas = 0
            if total == 0:
                break

            if total < 2 and total > 0:
                print(f'sobrou R$ {total} que não pode ser sacado em notas.')
                break 

    print('=' * 20)
    print('volte sempre')

caixa_eletronico()