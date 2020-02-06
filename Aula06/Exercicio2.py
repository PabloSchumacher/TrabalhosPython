#--- Exercício 2 - For
#--- Escreva programa que leia um número inteiro
#--- Calcule a taboada do número informado
#--- Imprima a taboada com a conta completa (n * i = r)

n = float(input('Informe o número: '))
for i in range(0,11):
    print(f'{n} x {i} = {n*i}')