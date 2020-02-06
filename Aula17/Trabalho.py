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

def dadosclientes(iduser, nome, idade, cpf, telefone, pais, estado, cidade, bairro, rua, n, complemento):
    dados = {'id':iduser, 'nome':nome, 'idade':idade, 'cpf':cpf, 'telefone':telefone, 'pais':pais, 'estado':estado, 'cidade':cidade, 'bairro':bairro, 'rua':rua, 'n':n, 'complemento':complemento}
    return dados

listacadastro = []
def cadastroclientes():
    cadastro = open('TrabalhosPython/Aula17/cadastro.txt','a')
    cadastro.write(f'{dados["id"]};{dados["nome"]};{dados["idade"]};{dados["cpf"]};{dados["telefone"]};{dados["pais"]};{dados["estado"]};{dados["cidade"]};{dados["bairro"]};{dados["rua"]};{dados["n"]};{dados["complemento"]}\n')
    cadastro.close()
    return cadastro

def dadosprodutos(idprod, nome, tipo, volume, preco):
    dadosprodutos = {'id':idprod, 'nome':nome, 'tipo':tipo, 'volume':volume, 'preco':preco}
    return dadosprodutos

listacadastroprodutos = []
def cadastroprodutos():
    cadastroprodutos = open('TrabalhosPython/Aula17/cadastroprodutos.txt','a')
    cadastroprodutos.write(f'{dadosprodutos["id"]};{dadosprodutos["nome"]};{dadosprodutos["tipo"]};{dadosprodutos["volume"]};{dadosprodutos["preco"]}\n')
    cadastroprodutos.close()
    return cadastroprodutos

def ler_dados():
    cadastro = open('TrabalhosPython/Aula17/cadastro.txt','r')
    lista_dados = []
    for linha in cadastro:
        linha = linha.strip()
        dados_dados = linha.split(';')
        
        dadoss = dadosclientes(dados_dados[0],dados_dados[1],dados_dados[2],dados_dados[3],dados_dados[4],dados_dados[5],dados_dados[6],dados_dados[7],dados_dados[8],dados_dados[9],dados_dados[10],dados_dados[11])
        lista_dados.append(dadoss)
    cadastro.close()
    return lista_dados


def ler_dadosprodutos():
    cadastroprodutos = open('TrabalhosPython/Aula17/cadastroprodutos.txt','r')
    lista_dados = []
    for linha in cadastroprodutos:
        linha = linha.strip()
        dados_dadosprodutos = linha.split(';')
        dadossprodutos = dadosprodutos(dados_dadosprodutos[0],dados_dadosprodutos[1],dados_dadosprodutos[2],dados_dadosprodutos[3],dados_dadosprodutos[4])
        listacadastroprodutos.append(dadossprodutos)
    cadastroprodutos.close()
    return listacadastroprodutos

lista_de_vendas = []
ler_dados()
ler_dadosprodutos()
while True:
    opcao = input(menu)

    if opcao == '1':
        iduser = int(input('Informe o ID: '))
        nome = input('Informe o nome completo: ')
        idade = int(input('Informe a data de nascimento: '))
        cpf = input('Informe o CPF: ')
        telefone = input('Informe o telefone para contato: ')
        pais = input('Informe o país: ')
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        bairro = input('Informe o bairro: ')
        rua = input('Informe a rua: ')
        n = int(input('Informe o número da casa: '))
        complemento = input('Informe o complemento: ')
        dados = dadosclientes(iduser, nome, idade, cpf, telefone, pais, estado, cidade, bairro, rua, n, complemento)
        cadastro = cadastroclientes()

    elif opcao == '2':
        print(ler_dados())

    elif opcao == '3':
        idprod = int(input('Informe o ID: '))
        nome = input('Informe o nome: ')
        marca = input('Informe a marca: ')
        validade = input('Informe a validade: ')
        garantia = input('Informe a garantia: ')
        dadosprodutos = dadosprodutos(idprod, nome, marca, validade, garantia)
        cadastroprodutos = cadastroprodutos()

    elif opcao == '4':
        print(ler_dadosprodutos())

    elif opcao == '5':
        vendas = open('TrabalhosPython/Aula17/vendas.txt','a')
        venda = input('Informe o codigo da venda: ')
        data = input('Informe a data da venda: ')
        cliente = input('Informe o código do cliente: ')
        produto = input('Informe o código da cerveja: ')
        quantidade = input('Informe a quantidade de cerveja comprada: ')
        dicionarioclipro = {'idvenda':venda,'data':data,'idcliente':cliente,'idproduto':produto,'quantidade':quantidade}
        lista_de_vendas.append(dicionarioclipro)
        vendas.write(f'{venda};{data};{cliente};{produto};{quantidade}\n')
        vendas.close()

    # elif opcao == '6':
    #     # print('Relatório de Vendas')
    #     vendas = open('Aula17/vendas.txt','r')
    #     cadastroprodutos = open('Aula17/cadastroprodutos.txt','r')
    #     cadastroclientes = open('Aula17/cadastro.txt','r')
    #     relatoriodevendas = open('Aula17/relatoriodevendas.txt','a')
    #     # codigo = input('das')
    #     # for dado in dadosprodutos:
    #     #   if pessoa['idprod'] == codigo:


         
    #     vendas.close()
    #     cadastroprodutos.close()
    #     cadastroclientes.close()

    elif opcao == '7':
        print('Sair')
        break

    else:
        print('Valor Inválido')
