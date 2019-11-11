#Aula 4
# Fazer um programa que leia 2 números
# Realize as 4 operações matemáticas
# Imprima o resultado das operações
# Diga qual número é o maior dos dois números
import os

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print("\n" * os.get_terminal_size().lines)

print('='*50,'\n')

resultado = n1+n2
print(f'{n1} + {n2} é igual a: {resultado}')
resultado = n1/n2
print(f'{n1} / {n2} é igual a: {resultado}')
resultado = n1-n2
print(f'{n1} - {n2} é igual a: {resultado}')
resultado = n1*n2
print(f'{n1} * {n2} é igual a: {resultado}')

if n1 > n2:
    print(f'O maior número entre {n1} e {n2} é: {n1}.')
elif n1 == n2:
    print('O dois números são iguais.')
else:
    print(f'O maior número entre {n1} e {n2} é {n2}.')

print('\n','='*50)