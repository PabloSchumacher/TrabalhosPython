embarque = ['Presidiário','Policial' , 'Piloto', 'Oficial1', 'Oficial2', 'Chefe', 'Comissária1','Comissária2']

def txt_terminal(embarque):
    lista = []
    dados = ','.join(embarque) # Convertendo uma lista em String e atribuindo ela a variável dados
    arquivo = open('Aula29/lista_terminal.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    lista.append(dados) # Inserindo na lista os dados do arquivo
    arquivo.close() # Fehando arquivo
    return lista

def txt_aviao(aviao):
    dados = ','.join(aviao)       
    arquivo = open('Aula29/lista_aviao.txt', 'w') # Criando arquivo
    arquivo.write(dados)  # Inserindo conteúdo no arquivo
    arquivo.close() # Fehando arquivo