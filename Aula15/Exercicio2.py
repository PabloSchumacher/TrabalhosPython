def salvcerv(cerveja):
    ex2 = open('ex2.txt','a')
    ex2.write(f"{cerveja['marca']};{cerveja['tipo']};{cerveja['teor']}\n")
    ex2.close()

def leitura():
    lista = []
    ex2 = open('ex2.txt','r')
    for linha in ex2:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0], 'tipo':lista_linha[1], 'teor':lista_linha[2]}
        lista.append(cerveja)
    ex2.close()
    return lista

marca = input('Informe a marca: ')
tipo = input('Informe o tipo: ')
teor = input('Informe o teor: ')

cerveja = {'marca':marca, 'tipo':tipo, 'teor':teor}

salvcerv(cerveja)

for i in leitura():
    print(f"{i['marca']} - {i['tipo']} - {i['teor']}")