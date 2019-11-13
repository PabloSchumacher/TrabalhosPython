#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

nomes = []
notas = []

for i in range(1,11):
    nome = [input(f'Informe o {i}° nome: ')]
    nomes.append (nome)

    for i in range(1,5):
        nota = [float(input(f'Informe a {i}° nota: '))]
        notas.append (nota)

for x in nomes and notas:
    print(f'Nome: {nome}, Nota: {nota}')
    

