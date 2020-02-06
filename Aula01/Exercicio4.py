#--- Exercicio 4  - Impressão de dados com a função Print
#--- Crie a tela inicial para um sistema de compra de bebidas 
#--- A tela deve conter cabeçalho, menu, tela de boas vindas e rodapé

print('=-='*55,'\n')

nome = input('Olá, por favor insira seu nome: ')
print (f'Bem vindo {nome}!','\n')
bebida = input(f'{nome}, digite o nome da bebida que deseja comprar: ')
qtd = float(input(f'{nome}, digite a quantidade em Litros que deseja comprar: '))

print('\n','=-='*55)