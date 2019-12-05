# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing

#1:
def ler():
    arquivo = open('C:\\Users\\900157\\Documents\\GitHub\\TrabalhosPython\\Aula19\\exercicios\\cadastro.txt','r')
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

#2:
lista = ler()
lista_maiores = []
maiores = open('C:\\Users\\900157\\Documents\\GitHub\\TrabalhosPython\\Aula19\\exercicios\\maiores.txt','a')
menores = open('C:\\Users\\900157\\Documents\\GitHub\\TrabalhosPython\\Aula19\\exercicios\\menores.txt','a')
for dicionario in lista:
        if int(dicionario['Idade']) >=18:
            maiores.write(f'{dicionario["ID"]};{dicionario["Nome"]};{dicionario["Idade"]};{dicionario["Sexo"]};{dicionario["Email"]};{dicionario["Telefone"]}\n')
        else:
            menores.write(f'{dicionario["ID"]};{dicionario["Nome"]};{dicionario["Idade"]};{dicionario["Sexo"]};{dicionario["Email"]};{dicionario["Telefone"]}\n')
maiores.close()
menores.close()

#3:
def contar(lista):
    for dicionario in lista:
        if dicionario['Sexo'] == "m":
            dicionario['Sexo'].count("m")
            a = dicionario['Sexo'].count("m")
            print(a)
contar(lista)            