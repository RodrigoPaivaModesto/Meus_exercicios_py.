#verificador_ano_bissexto

def verificador_ano_bissexto():
    ano = int(input('Digite o ano: '))

    if (ano %4 == 0 and ano %100 != 0) or (ano %400 ==0):
        print('sim')
    else:
        print('não')

    
verificador_ano_bissexto()


#ou pode ser assim também


def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano %400 == 0):
        return True
        
    else:
        return False
    
resultado = eh_bissexto(2028)  

print(f'o ano é bissexto ? {resultado}')






