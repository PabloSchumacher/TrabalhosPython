#Criar um programa que leia 4 notas
#Imprima a maior nota
#Imprima a menor nota
#Imprima a média
#Imprima se o aluno foi aprovado ou reprovado (Média 7.0)

import os

n1 = float(input('Digita a primeira nota: '))
print("\n" * os.get_terminal_size().lines)
n2 = float(input('Digita a segunda nota: '))
print("\n" * os.get_terminal_size().lines)
n3 = float(input('Digita a terceira nota: '))
print("\n" * os.get_terminal_size().lines)
n4 = float(input('Digita a quarta nota: '))
print("\n" * os.get_terminal_size().lines)
media = float((n1+n2+n3+n4)/4)

print ('=-='*30)
print('\n')

if n1 == n2 == n3 == n4:
    print ('As quatro notas são iguais')

if n1 > n2 and n1 > n3 and n1 > n4:
    print (f'A maior nota é: {n1}')
elif n2 > n3 and n2 > n4:
    print (f'A maior nota é: {n2}')
elif n3 > n4:
    print (f'A maior nota é: {n3}')
else:
    print (f'A maior nota é: {n4}')

if n1 < n2 and n1 < n3 and n1 < n4:
    print (f'A menor nota é: {n1}')
elif n2 < n3 and n2 < n4:
    print (f'A menor nota é: {n2}')
elif n3 < n4:
    print (f'A menor nota é: {n3}')
else:
    print (f'A menor nota é: {n4}')

if media >= 7:
    print (f'Sua média é {media} e você está aprovado!')
else:
    print (f'Sua média é {media} e você está reprovado.')

print('\n')
print ('=-='*30)