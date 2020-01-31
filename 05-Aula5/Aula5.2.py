# 3 -
# Cadastro Produtos Mercado Tech
# Solicitar o nome do produto
# Solicitar a categoria do produto (Alcoolico e Não Alcoolico)
# Exibir o produto cadastrado

nome = input('Informe o nome do produto: ')
print ('Informe a categoria do produto: ')
categoria = input('1- Alcoolico 2- Não Alcoolico: ')

if categoria != ('1') or ('2'):
    print('Inválido, tente de novo')
    categoria = input('1- Alcoolico 2- Não Alcoolico: ')

if categoria == ('1'):
    categoria = ('Alcoolico')
elif categoria == ('2'):
    categoria = ('Não Alcoolico')

print(f'Nome do produto: {nome}')
print(f'Categoria do produto: {categoria}')