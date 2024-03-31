string = input("Digite uma string: ")

def inverter(texto):
    txtInvertido = ''
    for char in texto:
        txtInvertido = char + txtInvertido
    return txtInvertido

print(inverter(string))