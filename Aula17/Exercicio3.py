# def cadastro_cliente(numero):
#     dados_cliente = ['codigo_cliente', 'CPF', 'nome_completo',
#                     'data_de_nascimento', 'estado', 'cidade',
#                     'cep', 'bairro', 'rua', 'numero_casa', 'complemento']
#     lista = []

#     for i in range(numero):
#         dicionario = {}
#         for i in dados_cliente:
#             dicionario[i]=input(f'{i}: ')
#         lista.append(dicionario)
#     return lista

# numero=int(input('Digite número de cadastros que serão realiados: '))
# lista_cadastro = cadastro_cliente(numero)
# print (lista_cadastro)

# arquivo = open('Aula17/clientes.txt','a')
# for cliente in arquivo:
#     salvar = f'{cliente['codigo_cliente']}'

# arquivo.write()

# arquivo.close()