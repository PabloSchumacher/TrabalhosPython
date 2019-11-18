#--- Exercicio 2  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia os dados de um cliente
#--- Cliente: Nome, Sobrenome, ano de nascimento
#--- Exiba uma mensagem de boas vindas para o cliente
#--- Exiba um menu: Produtos alcoolicos e Produtos não alcoolicos, Sair
#--- Caso o cliente seja menor de idade o item 'produtos alcoolicos' não deve ser exibido
#--- Leia a opção digitada e crie uma tela para cada opção

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
nascimento = float(input('Digite seu ano de nascimento: '))

print('\n'f'Bem vindo {nome} {sobrenome}\n')

if nascimento <= 2001:
    escolhe = int(input('Qual menu você deseja acessar? 1- Produtos Alcoolicos 2- Produtos Não Alcoolicos 3-Sair: '))
    if escolhe == 1:
        print('Vodka: R$10,00 / Cerveja Kaiser: R$1,50 / Corote: R$5,00.')
    elif escolhe == 2:
        print('Guaraná: R$5,00 / Sprite: R$5,00 / Energético: R$7,00.')
    elif escolhe ==3:
        print:('Volte sempre!')
else:
    escolhe = int(input('Qual menu você deseja acessar? 1- Produtos Não Alcoolicos 2-Sair: '))
    if escolhe == 1:
        print('Guaraná: R$5,00 / Sprite: R$5,00 / Energético: R$7,00.')
    elif escolhe == 2:
        print:('Volte sempre!')