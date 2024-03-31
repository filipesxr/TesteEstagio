num = int(input("Digite um número: "))

def conferir(num):
    a = 0
    b = 1
    resultado = []
    while a <= num:
        resultado.append(a)
        proximo_numero = a + b
        a = b
        b = proximo_numero

    if num in resultado:
        print("Este número PERTENCE a sequência de Fibonacci")
    else:
        print("Este número NÃO PERTENCE a sequência de Fibonacci")
    return resultado

print(conferir(num))