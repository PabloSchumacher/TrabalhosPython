lista = [1,2,3,4,5,6,7]
rotacao = int(input('Quantas rotações você deseja fazer?: '))
print(f'Lista inicial: {lista}')

for i in range(rotacao):
    lista.insert(0, lista[-1])
    del(lista[-1])
print(f'Lista final: {lista}')