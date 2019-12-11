menu = ('''
##################################################################################
#                                FESTA DA CERVEJA                                #
##################################################################################

1 - Cadastro de Clientes
2 - Ver Clientes Cadastrados
3 - Cadastro de Produtos
4 - Ver produtos cadastrados
5 - Vendas
6 - Relatório de Vendas
7 - Sair
Informe qual menu você qual opção você deseja: ''')    

def dados(iduser, nome, idade, cpf, telefone, pais, estado, cidade, rua, n):
    dados = {'id':iduser, 'nome':nome, 'idade':idade, 'cpf':cpf, 'telefone':telefone, 'pais':pais, 'estado':estado, 'cidade':cidade, 'rua':rua, 'n':n}
    return dados

listacadastro = []
def cadastro():
    cadastro = open('Aula17/cadastro.txt','a')
    cadastro.write(f'{dados["id"]};{dados["nome"]};{dados["idade"]};{dados["cpf"]};{dados["telefone"]};{dados["pais"]};{dados["estado"]};{dados["cidade"]};{dados["rua"]};{dados["n"]}\n')
    cadastro.close()
    return cadastro

def dadosprodutos(idprod, nome, marca, validade, garantia):
    dadosprodutos = {'id':idprod, 'nome':nome, 'marca':marca, 'validade':validade, 'garantia':garantia}
    return dadosprodutos

listacadastroprodutos = []
def cadastroprodutos():
    cadastroprodutos = open('Aula17/cadastroprodutos.txt','a')
    cadastroprodutos.write(f'{dadosprodutos["id"]};{dadosprodutos["nome"]};{dadosprodutos["marca"]};{dadosprodutos["validade"]};{dadosprodutos["garantia"]}\n')
    cadastroprodutos.close()
    return cadastroprodutos

def ler_dados():
    cadastro = open('Aula17/cadastro.txt','r')
    lista_dados = []
    for linha in cadastro:
        linha = linha.strip()
        dados_dados = linha.split(';')
        dadoss = dados(dados_dados[0],dados_dados[1],dados_dados[2],dados_dados[3],dados_dados[4],dados_dados[5],dados_dados[6],dados_dados[7],dados_dados[8],dados_dados[9])
        lista_dados.append(dadoss)
    cadastro.close()
    return lista_dados


def ler_dadosprodutos():
    cadastroprodutos = open('Aula17/cadastroprodutos.txt','r')
    lista_dados = []
    for linha in cadastroprodutos:
        linha = linha.strip()
        dados_dadosprodutos = linha.split(';')
        dadossprodutos = dadosprodutos(dados_dadosprodutos[0],dados_dadosprodutos[1],dados_dadosprodutos[2],dados_dadosprodutos[3],dados_dadosprodutos[4])
        listacadastroprodutos.append(dadossprodutos)
    cadastroprodutos.close()
    return listacadastroprodutos

while True:
    opcao = input(menu)

    if opcao == '1':
        iduser = input('Informe o ID: ')
        nome = input('Informe o nome: ')
        idade = input('Informe a idade: ')
        cpf = input('Informe o CPF: ')
        telefone = input('Informe o telefone para contato: ')
        pais = input('Informe o país: ')
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        rua = input('Informe a rua: ')
        n = input('Informe o número da casa: ')
        dados = dados(iduser, nome, idade, cpf, telefone, pais, estado, cidade, rua, n)
        cadastro = cadastro()

    elif opcao == '2':
        print(ler_dados())

    elif opcao == '3':
        idprod = input('Informe o ID: ')
        nome = input('Informe o nome: ')
        marca = input('Informe a marca: ')
        validade = input('Informe a validade: ')
        garantia = input('Informe a garantia: ')
        dadosprodutos = dadosprodutos(idprod, nome, marca, validade, garantia)
        cadastroprodutos = cadastroprodutos()

    elif opcao == '4':
        print(ler_dadosprodutos())

    elif opcao == '5':
        print('Vendas')

    elif opcao == '6':
        print('Relatório de Vendas')

    elif opcao == '7':
        print('Sair')
        break

    else:
        print('Valor Inválido')
