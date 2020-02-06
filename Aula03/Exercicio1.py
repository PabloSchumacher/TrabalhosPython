#--- Exercicio 1  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que leia dois números inteiros
#--- Realize as 4 operações matemáticas básicas com os números lidos
#--- Imprima os resultados das operações 
#--- Informe qual número é maior ou se os dois são iguais

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} - {n2} = {n1-n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} * {n2} = {n1*n2}')

if n1 > n2:
    print(f'O maior número é {n1}.')
elif n2 == n2:
    print(f'Os dois números são iguais.')
else:
    print(f'O máior número é {n2}.')