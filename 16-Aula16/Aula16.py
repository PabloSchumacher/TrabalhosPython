# Aula 16 - 29-11-2019
# ??????????

#Cadastro de playlist
#Lendo musica, artista e album

from faixa import criar_faixa, salvar_faixa, ler_faixa

print('='*50)

musica = input('Digite o nome da musica: ')
artista = input('Digite o nome do(a) artista: ') 
album = input('Digite o nome do album: ')

faixa = criar_faixa(musica,artista,musica)
salvar_faixa(faixa)
lista = ler_faixa()

for f in lista:
    print(f'{faixa["musica"]} - {faixa["artista"]} - {faixa["album"]}')