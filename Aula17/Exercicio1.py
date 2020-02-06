menu = ('''
##################################################################################
#                              Cadastro de Playlist                              #
##################################################################################

1 - Cadastro de banda
2 - Cadastro do album
3 - Cadastro da musica
4 - Sair
Informe qual menu você qual opção você deseja: ''')

lista_banda = []
lista_album = []
lista_musica = []

while True:
    opcao = input(menu)
    if opcao == '1':
        lista_banda.append(input('Digite o nome da banda: '))
    elif opcao == '2':
        lista_album.append(input('Digite o nome do album: '))
    elif opcao == '3':
        lista_musica.append(input('Digite o nome da música: '))
    elif opcao == '4':
        print(f'Bandas Cadastradas: {lista_banda}\nAlbuns Cadastrados: {lista_album}\nMusicas Cadastradas: {lista_musica}')
        break
    else:
        print('\n''Opção Inválida!')