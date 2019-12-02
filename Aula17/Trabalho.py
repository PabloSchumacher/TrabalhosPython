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

while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Cliente')
    elif opcao == '2':
        print('Ver Clientes Cadastrados')
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Ver produtos cadastrados')
    elif opcao == '5':
        print('Vendas')
    elif opcao == '6':
        print('Relatório de Vendas')
    elif opcao == '7':
        print('Sair')
        break
    else:
        print('Valor Inválido')
    
    