#--- Exercicio 2 - Dicionários
#--- Escreva um programa que leia os dados de 11 jogadores
#--- Jogador: Nome, Posicao, Numero, PernaBoa
#--- Crie um dicionario para armazenar os dados
#--- Imprima todos os jogadores e seus dados

lista_jogador = []

for i in range(0,11):
    dicionario_jogador = {'Nome':'', 'Posicao':'', 'Numero':'','Pernaboa':''}
    dicionario_jogador['Nome'] = input(f'Digite o nome do {i+1}° jogador: ')
    dicionario_jogador['Posicao'] = input(f'Digite a posição do {i+1}° jogador: ')
    dicionario_jogador['Numero'] = int(input(f'Digite o número do {i+1}° jogador: '))
    dicionario_jogador['Pernaboa'] = input(f'Digite o perna boa do {i+1}° jogador: ')
    lista_jogador.append(dicionario_jogador)

for j in lista_jogador:
    print(f"Nome: {dicionario_jogador['Nome']} - Posição: {dicionario_jogador['Posicao']} - Numero: {dicionario_jogador['Numero']} - Pernaboa: {dicionario_jogador['Pernaboa']}")

