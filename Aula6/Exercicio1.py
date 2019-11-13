#--- Exercicio 1 - listas
#--- Escreva programa que leia o nome de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima a lista

nomes = []
for i in range(1,11):
    nome = [input(f'Informe o {i}° nome: ')]
    nomes.append (nome)

for y in nomes:
    print(f'O nome informado é {y}')