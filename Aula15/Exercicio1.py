def salvar_pessoa(pessoa_dicionario):
    ex1 = open('Ex1.txt','a')
    ex1.write(f"{pessoa_dicionario['nome']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    ex1.close()

def ler():
    lista = []
    ex1 = open('Ex1.txt','r')
    for linha in ex1:
        linha = linha.strip()
        lista_linha = linha.split(';')
        pessoa = {'nome':lista_linha[0], 'sobrenome':lista_linha[1],'idade':lista_linha[2]}
        lista.append(pessoa)
    ex1.close()
    return lista

nome = input('Digite seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
idade = int(input('Digite a sua idade: '))

pessoa = {'nome':nome, 'sobrenome':sobrenome,'idade':idade}
salvar_pessoa(pessoa)
for l in ler():
    print(f"{l['nome']} - {l['sobrenome']} - {l['idade']}")


# print (ler())

# ex1 = open('ex1','r')
# for linha in ex1:
#     print(linha)
# ex1.close()