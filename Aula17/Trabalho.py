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

def dadosclientes(iduser, nome, idade, cpf, telefone, pais, estado, cidade, rua, n):
    dados = {'id':iduser, 'nome':nome, 'idade':idade, 'cpf':cpf, 'telefone':telefone, 'pais':pais, 'estado':estado, 'cidade':cidade, 'rua':rua, 'n':n}
    return dados

listacadastro = []
def cadastroclientes():
    cadastro = open('Aula17/cadastro.txt','a')
    cadastro.write(f'ID: {dados["id"]};Nome: {dados["nome"]};Idade: {dados["idade"]};CPF: {dados["cpf"]};Telefone: {dados["telefone"]};País: {dados["pais"]};Estado: {dados["estado"]};Cidade: {dados["cidade"]};Rua: {dados["rua"]};Número: {dados["n"]}\n')
    cadastro.close()
    return cadastro

def dadosprodutos(idprod, nome, marca, validade, garantia):
    dadosprodutos = {'id':idprod, 'nome':nome, 'marca':marca, 'validade':validade, 'garantia':garantia}
    return dadosprodutos

listacadastroprodutos = []
def cadastroprodutos():
    cadastroprodutos = open('Aula17/cadastroprodutos.txt','a')
    cadastroprodutos.write(f'ID: {dadosprodutos["id"]};Nome: {dadosprodutos["nome"]};Marca: {dadosprodutos["marca"]};Validade: {dadosprodutos["validade"]};Garantia: {dadosprodutos["garantia"]}\n')
    cadastroprodutos.close()
    return cadastroprodutos

def ler_dados():
    cadastro = open('Aula17/cadastro.txt','r')
    lista_dados = []
    for linha in cadastro:
        linha = linha.strip()
        dados_dados = linha.split(';')
        dadoss = dadosclientes(dados_dados[0],dados_dados[1],dados_dados[2],dados_dados[3],dados_dados[4],dados_dados[5],dados_dados[6],dados_dados[7],dados_dados[8],dados_dados[9])
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

lista_de_vendas = []
ler_dados()
ler_dadosprodutos()
while True:
    opcao = input(menu)

    if opcao == '1':
        iduser = int(input('Informe o ID: '))
        nome = input('Informe o nome: ')
        idade = int(input('Informe a idade: '))
        cpf = input('Informe o CPF: ')
        telefone = input('Informe o telefone para contato: ')
        pais = input('Informe o país: ')
        estado = input('Informe o estado: ')
        cidade = input('Informe a cidade: ')
        rua = input('Informe a rua: ')
        n = int(input('Informe o número da casa: '))
        dados = dadosclientes(iduser, nome, idade, cpf, telefone, pais, estado, cidade, rua, n)
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
        vendas = open('Aula17/vendas.txt','a')
        cliente = input('Informe o ID do cliente: ')
        produto = input('Informe o ID do produto: ')
        dicionarioclipro = {'iduser':cliente,'idprod':produto}
        lista_de_vendas.append(dicionarioclipro)
        vendas.write(f'ID Cliente: {cliente},ID Produto: {produto}\n')
        vendas.close()
        print(f'Venda registrada para cliente com ID: {cliente} e produto com iD: {produto}')

    elif opcao == '6':
        # print('Relatório de Vendas')
        vendas = open('Aula17/vendas.txt','r')
        cadastroprodutos = open('Aula17/cadastroprodutos.txt','r')
        cadastroclientes = open('Aula17/cadastro.txt','r')
        relatoriodevendas = open('Aula17/relatoriodevendas.txt','a')
        # codigo = input('das')
        # for dado in dadosprodutos:
        #   if pessoa['idprod'] == codigo:


         
        vendas.close()
        cadastroprodutos.close()
        cadastroclientes.close()

    elif opcao == '7':
        print('Sair')
        break

    else:
        print('Valor Inválido')
