n = int(input('Insira o número: '))

def solucao(n):
    binario = bin(n)
    binario = binario.replace('0b','')
    binario = binario
    maiorgap = 0
    for i in binario:
        print(i)
        if i == '1':
            x = binario[i] +1
            print(x)


solucao(n)
