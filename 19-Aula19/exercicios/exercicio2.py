# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email', 'idade']

pess = [['Alex', 'Paulo', 'Pedro', 'Mateus', 'Carlos', 'João', 'Joaquim'],
        ['4799991', '4799992', '4799993', '4799994',
         '4799995', '4799996', '4799997'],
        ['a@a.com', 'b@b.com', 'c@c.com', 'd@d.com',
         'e@e.com', 'f@f.com', 'g@g.com'],
        ['18', '25', '40', '16', '15', '19', '17']
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#

nome = pess[0]
telefone = pess[1]
email = pess[2]
idade = pess[3]

for j in range(len(idade)):
        if int(pess[3][j]) >=18:
                dicionario = {'Nome': nome[j], 'Email': email[j], 'Idade': idade[j], 'Telefone': telefone[j]}
                print (dicionario)

#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha
# (não prescisa usar o f-string, .format())
#
lista = []
for j in range(len(idade)):
        dicionario = {'Nome': nome[j], 'Email': email[j], 'Idade': idade[j], 'Telefone': telefone[j]}
        lista.append(dicionario)
for i in lista:
        print(i)

#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha
# (usando o f-string)

lista = []
for j in range(len(idade)):
    dicionario = {'Nome': nome[j], 'Email': email[j],
                  'Idade': idade[j], 'Telefone': telefone[j]}
    lista.append(dicionario)
for dicio in lista:
    valores = ''
    for i in dicio:
        valores = valores + (f'{i}: {dicio[i]}, ')
    print(valores)
