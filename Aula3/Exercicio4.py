#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

usuario = input('Digite o nome de usuário: ')
senha = int(input('Digite a senha: '))
if usuario == 'joj' and senha == 123:
    print('Seja bem vindo!')
else:
    print('Falha no login.')