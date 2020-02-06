def converter_tabela_dicionario(lista_tuplas):
    lista_endereco = []
    for e in lista_tuplas:
        dicionario_endereco = {'Id': 0, 'Logradouro' : '', 'Numero': 0, 'Complemento' : '', 'Bairro': '', 'Cidade': '', 'Cep': 0}
        dicionario_endereco['Id'] = e[0]
        dicionario_endereco['Logradouro'] = e[1]
        dicionario_endereco['Numero'] = e[2]
        dicionario_endereco['Complemento'] = e[3]
        dicionario_endereco['Bairro'] = e[4]
        dicionario_endereco['Cidade'] = e[5]
        dicionario_endereco['Cep'] = e[6]
        lista_endereco.append(dicionario_endereco)
    return lista_endereco