#conversor de temperatura

def conversor_de_temperatura_fahrenheit(celsius):
    celsius = float(input('digite a temperatura: '))
    fahrenheit = (celsius * 1.8) + 32

    return fahrenheit

print(conversor_de_temperatura_fahrenheit(30))

    