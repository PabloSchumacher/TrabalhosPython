#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

nomes = []
notas = []
media = 0
n1 = 0
n2 = 1
n3 = 2
n4 = 3

for i in range(0,2):
    nomes.append (input(f'Informe o {i+1}° nome: '))

    for j in range(0,4):
        notas.append (float(input(f'Informe a {j+1}° nota: ')))

for x in nomes:
    media = (notas[n1]+notas[n2]+notas[n3]+notas[n4])/4
    resultado = 'Reprovado'
    if media >7:
        resultado = 'Aprovado'
    print(f'Nome: {x}, Média: {media} Resultado:{resultado}')
    
    n1= n1+4
    n2= n2+4
    n3= n3+4
    n4= n4+4