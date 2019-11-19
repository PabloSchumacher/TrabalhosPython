# Aula 8 - 18-11-2019
# Tuplas

numeros = [1,4,6]
usuario = {'nome':'user','passw':123456}
pessoa = ('pablo','schumacher',0,45.5, numeros)

print(numeros)
print(usuario)
print(pessoa)

numeros[1] = 5
usuario['passwd'] = 456123
lista_pessoas = []
lista_pessoas.append(pessoa)
pessoa[4][1] = 6
print(pessoa[4][1])