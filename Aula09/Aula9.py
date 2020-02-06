# Aula9 - 10-11-2019
#--- Crie um programa que:
#---1 - Leia dois números inteiros
#---2 - Calcule a soma entre os dois números através de um método
#---3 - Calcule a subtração entre os dois números através de um método
#---4 - Calcule a multiplicação entre os dois números através de um método
#---5 - Calcule a divisão inteira entre os dois números através de um método
#---6 - Calcule a divisão fracionada entre os dois números através de um método
#---7 - Calcule a o resto da divisão entre os dois números através de um método
#---8 - Calcule a raiz entre os dois números através de um método
#---9 - Separar os métodos em outro arquivo

from MetodosExercicio import soma,sub,mult,divfra,divint,restodiv,raiz1,raiz2

print('\n','=-='*30,'\n')

n1 = float(input('Informe o 1° número: '))
n2 = float(input('Informe o 2° número: '))

print('\n')

mais = soma(n1,n2)
menos = sub(n1,n2)
vezes = mult(n1,n2)
divisaofracionada = divfra(n1,n2)
divisaointeira = divint(n1,n2)
restodivisao = restodiv(n1,n2)
raizquadradan1 = raiz1(n1,n2)
raizquadradan2 = raiz2(n1,n2)

print(f'A soma entre {n1} e {n2} é: {mais}')
print(f'a subtração entre {n1} e {n2} é: {menos}')
print(f'A multiplicação entre {n1} e {n2} é :{vezes}')
print(f'A divisão fracionada entre {n1} e {n2} é: {divisaofracionada}')
print(f'A divisão inteira entre {n1} e{n2} é: {divisaointeira}')
print(f'O resto da divisão entre {n1} e {n2} é: {restodivisao}')
print(f'A raiz de {n1} é: {raizquadradan1} e a raiz de {n2} é: {raizquadradan2}')

print('\n','=-='*30,'\n')