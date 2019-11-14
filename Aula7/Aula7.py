# Aula 7 - 14-11-2019
# Dicionarios

lista = []
dicionario = { 'nome':'Pablo', 'sobrenome':'Schumacher' }

print(dicionario)
print(dicionario['sobrenome'])

nome = 'Pablo'
lista_notas = [10,10,10,10]
media = sum(lista_notas)/ len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome':nome, 'Lista_Notas':lista_notas, 'Media':media, 'Situacao':situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Lista_Notas']} - {dicionario_alunos['Situacao']}")