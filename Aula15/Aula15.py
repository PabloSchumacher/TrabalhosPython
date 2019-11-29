# Aula 15 - 28-11-2019
# Manipulação de arquivos

# arquivo = open('aula15.txt','a')
# arquivo.write('Voltoline \n')
# arquivo.close()

arquivo = open('aula15.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()
