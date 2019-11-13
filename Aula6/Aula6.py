# Aula 6 - 13-11-2019
# Listas

#Inicialização de uma variavel do tipo lista
lista1 = []
#Inicialização de uma variavel do ipo lista, com elementos
lista2 = ['Marcela', 'Nicole', 'Matheus',10]
#Lista com inteiros
lista3 = [1,2,3,5]
#Lista com tipos diferentes
lista4 = [1, "Maykon",12.5]

#Impressão de listas criadas
print(lista1)
print(lista2)
print(lista3)
print(lista2[2])

#...Adicionando elementos em uma lista ja criada

lista1.append(lista2)
lista1.append(lista3)

#Imprimindo listas modificadas
print (lista1)
print (lista2)
print (lista3)

#...Criação de listas com dadosvindos de função Input
lista_duvida = [input('Digite seu nome: '),input('Ditige seu sobrenome: ')]
print (lista_duvida)

#Recuperando um dado de uma posição específica
posicao = int(input('Digite a posição: '))
print(lista2[posicao-1])
