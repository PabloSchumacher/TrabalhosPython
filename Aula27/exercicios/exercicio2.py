# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if lista[0] is lista[1]:
    print('lista[0] é igual a lista[1]')
elif lista[0] == lista[1]:
    print('lista[0] é igual a lista[1]')
else:
    print('As lstas são diferentes')

# 2) Qual é o maior valor destas duas listas 
if lista[0] > lista[1]:
    print('A maior lista é a lista[1]')
else:
    print('A maior lista é a lista[2]')


# 3) Qual é o maior valor de cada lista
print(f'O maior valor da lista[0] é: {max(lista[0])}\nO maior valor da lista[1] é: {max(lista[1])}')

# 4) Há o número 10 dentro da lista[0]?
dez = 10
if dez not in lista[0]:
    print('O número 10 não está na lista[0]')
else:
    print('O número 10 está na lista[0]')

# 5) Há o número 20 dentro da lista[1]?
vinte = 20
if vinte in lista[0]:
    print('O número 20 está na lista[0]')
else:
    print('O número 20 não está na lista[0]')

# 6) Quantos números da lista[0] tem dentro da lista[1]?
contador = 0
for i in lista[0]:
    if i in lista[1]:
        contador = contador+1
print(f'Existem {contador} elementos da lista[0] dentro da lista[1]')

# 7) Mostre os números da lista[0] que estão dentro da lista[1]
for i in lista[0]:
    if i in lista[1]:
        print(f'O número {i} está na lista[1]')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]
print('A soma da lista[0] com cada item da lista[1] é:')
for elemento in lista[1]:
    print(f'{sum(lista[0])+elemento}')

# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
if min(lista[0]) < min(lista[1]):
    menor = min(lista[0])
else:
    menor = min(lista[1])
if max(lista[0]) > max(lista[1]):
    maior = max(lista[0])
else:
    maior = max(lista[1])
resultado = (maior-menor)
print(f'O maior número da lista menos o menor número da lista é: {resultado}')
if resultado in lista[0] or resultado in lista[1]:
    print(f'O número {resultado} está em uma das listas')
else:
    print(f'O número {resultado} não está em uma das listas')

# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
if max(lista[0]) in lista[1]:
    print(f'O número {max(lista[0])} está na lista[1]')
else:
    print(f'O número {max(lista[0])} não está na lista[1]')

if min(lista[0]) in lista[0]:
    print(f'O número {max(lista[0])} está na lista[0]')
else:
    print(f'O número {max(lista[0])} não está na lista[0]')