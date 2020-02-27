n = int(input('Insira o número: '))

def solucao(n):
    binario = bin(n)
    binario = binario.replace('0b','')
    print(f'O seu número binário é: {binario}')
    maior_gap = 0
    gap = 0
    for i in binario:
        if i == '1':
            if gap > maior_gap:
                maior_gap = gap
            x = binario.index(i) #O problema ta nessa linha
            gap = 0
            while binario[x] == '0':
                gap += 1
                x += 1

    print(f'O maior gap é de: {maior_gap}')

solucao(n)