#--- Exercicio 1 - 
#--- Escreva o programa que leia os dados de cerveja
#--- Cerveja, Marca, Tipo, IBU, IBV, Volume
#--- Crie um dicionario para armazenar os dados
#--- Imprima os dados do dicionario (não dicionario completo)

marca = input('Informe a marca: ')
tipo = input('Informe o tipo: ')
ibu = input('Informe o ibu: ')
ibv = input('Informe o ibv: ')
volume = float(input('Informe o volume: '))

cerveja = {'Marca':marca, "Tipo":tipo, 'IBU':ibu, 'IBV':ibv, 'Volume':volume}
print(f"Marca: {cerveja['Marca']} - Tipo: {cerveja['Tipo']} - IBU: {cerveja['IBU']} - IBV: {cerveja['IBV']} - Volume: {cerveja['Volume'] }")