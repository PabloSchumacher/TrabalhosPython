n = int(input('Insira o número: '))

def solucao(n):
    binario = bin(n)
    binario = binario.replace('0b','')
    print(f'O seu número binário é: {binario}')
    valida_gap = False
    maior_gap = 0
    gap = 0
    for i in binario:
        if i == '1':
            if gap > maior_gap:
                maior_gap = gap
            gap = 0
            valida_gap = True
        elif i == '0' and valida_gap == True:
                gap += 1

    print(f'O maior gap é de: {maior_gap}')

solucao(n)