# Aula 20 - 05-12-2019


# Surgiu a necessidade de envio massivo de e-mails dos clientes cadastrados
# no arquivo cadastro1.txt 

# >>>> Fazer tudo com metodos <<<<<

# 1 - Para isso o programa necessita que separe os clientes maiores de 20 anos 
# em um arquivo separado chamado menores_de_idade.txt

def ler():
    arquivo = open('C:\\Users\\900157\\Documents\\GitHub\\TrabalhosPython\\Aula19\\exercicios\\cadastro1.txt','r')
    lista = []
    for linha in arquivo:
        linha_limpa =linha.strip()
        linha_lista = linha_limpa.split(';')

        id_user = linha_lista[0]
        nome = linha_lista[1]
        idade = linha_lista[2]
        sexo = linha_lista[3]
        email = linha_lista[4]
        telefone = linha_lista[5]

        dicionario = {'ID':id_user,'Nome':nome,'Idade':idade,'Sexo':sexo,'Email':email,'Telefone':telefone}
        lista.append(dicionario)
    arquivo.close()
    return lista

lista = ler()
menores_de_idade = open('C:\\Users\\900157\\Documents\\GitHub\\TrabalhosPython\\Aula19\\exercicios\\menores_de_idade.txt','a')
for dicionario in lista:
        if int(dicionario['Idade']) >=18:
            maiores.write(f'{dicionario["ID"]};{dicionario["Nome"]};{dicionario["Idade"]};{dicionario["Sexo"]};{dicionario["Email"]};{dicionario["Telefone"]}\n')
menores_de_idade.close()


# 2 - Separar os clientes femininos e salvar em um arquivo chamado feminini.txt

# 3 - Fazer um terminal de consulta onde se digita o código cliente e 
# imprima na tela o (f-string) o codigo, nome, idade, sexo, email, telefone.
# Se digitar um número que não exista, deverá aparecer uma mensagem dizendo
# "código não encontrado!" Se digitar 'S' (sair) o programa deve finalizar.

