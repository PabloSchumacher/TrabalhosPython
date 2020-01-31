# Aula 18 - 03-11-2019

# Festa da HBSIS

# 1 - Faça uma função que leia do arquivo cadastro.txt e retorne uma lista com dicionários.
# cada linha possui os dados na seguinte posição: codigo, nome, sexo, idade

# 2 - Como a entrada da festa é mais barata para mulheres (R$ 15,00) do que para os homens (R$ 35,00) 
# deve-se separar os dois em duas listas separadas e salvar em arquivos separados. Como é uma festa de arromba,
# menores de idade não podem entrar.

# 3 - Faça uma terceira função que ao digitar o código do participante ele imprima o nome do participante, 
# o valor do ingresso, e em caso de menores de idade apareça o texto "Entrada Proibida!"

# def __init__(self):
#     self.lista []

# def ler_cadastro(self):
#     arquivo = open('Aula18/exercicios/cadastro.txt','r')
#     lista = []
#     self.lista = [] arquivo: IO
#     for pessoas in arquivo:
#         pessoas = pessoas.strip().split(';')
#         dicionario = {'codigo':pessoas[0], 'nome':pessoas[1], 'sexo':pessoas[2], 'idade':pessoas[3]}
#         self.lista.append(dicionario)
#     arquivo.close()
#     return lista

# def lista_festa(lista_de_entrada):
#     lista_homens = []
#     lista_mulheres = []

#     for pessoa in  lista_de_entrada:
#         if int(pessoa['idade']) >=18:
#             if pessoa['sexo'] == 'f':
#                 lista_mulheres.append(pessoa)
#             else:
#                 print('não pode entrar')
#     salvar(lista_homens,'homens')
#     salvar(lista_mulheres,"mulheres")

# def salvar(lista,nome):
#     arquivo = open(f'Aula18/exercicios/{nome}.txt','a')
#     for pessoa in lista:
#         texto = (f"{pessoa['código']};{pessoa['nome']};{pessoa['sexo']};{pessoa['idade']}")
#         arquivo.write(texto)
#     arquivo.close()

# def consulta(lista_consulta_funcao, numero):
#     for lista_consulta in lista_consulta_funcao:
#         if int(lista_consulta['codigo']) == numero: 

#     if int(lista_consulta['idade']) >= 18:
#         if lista_consulta['sexo'] == 'f':
#             print(f"Nome: {lista_consulta['nome']} Valor ingresso: R$15,00 ")
#         else:
#             print(f"Nome: {lista_consulta['nome']} Valor ingresso: R$35,00 ")
#     else:
#         print('Nao Pode Entrar!')


# lista1 = ler_cadastro()
# lista_festa(lista1)

# while True:
#     a=int(input('Digite um numero'))
#     consulta(lista,a)