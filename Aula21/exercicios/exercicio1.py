# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.

a = 'n'
while a !='s':
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        soma = n1+n2
        multiplicacao = n1*n2
        divisao = n1/n2
        subtracao = n1-n2

        print(f'{n1} + {n2} = {soma}')
        print(f'{n1} / {n2} = {divisao}')
        print(f'{n1} * {n2} = {multiplicacao}')
        print(f'{n1} - {n2} = {subtracao}')
        controle = input("Digite 's' para sair: ")

    except (ValueError, ZeroDivisionError):
        print('\nVocê digitou o número errado animal!')



# a = 'n'
# while a !='s':
#     n1 = float(input('Digite o primeiro número: '))
#     n2 = float(input('Digite o segundo número: '))

#     soma = n1+n2
#     multiplicacao = n1*n2
#     divisao = n1/n2
#     subtracao = n1-n2

#     print(f'{n1} + {n2} = {soma}')
#     print(f'{n1} / {n2} = {divisao}')
#     print(f'{n1} * {n2} = {multiplicacao}')
#     print(f'{n1} - {n2} = {subtracao}')

#     controle = input("Digite 's' para sair:")