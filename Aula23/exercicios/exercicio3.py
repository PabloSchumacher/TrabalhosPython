# Aula 22 - 10-12-2019
# # Como Tratar e Trabalhar Erros!!!

# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!

class Cadastro:
    # Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.
    def ler(self):
        arquivo = open('C:\\Users\\900148\\Documents\\Dados\\GitHub\\AulasPython\\Aula_23\\exercicios\\cadastro2.txt','r')
        self.lista_dados = []
        for linha in arquivo:
            self.linha = linha.strip()
            self.dados_cliente = self.linha.split(';')
            self.dados = {'Codigo':self.dados_cliente[0],'Nome':self.dados_cliente[1],'Idade':self.dados_cliente[2],'Sexo':self.dados_cliente[3],'Email':self.dados_cliente[4],'Telefone':self.dados_cliente[5]}
            self.lista_dados.append(self.dados)



        arquivo.close()    
        return self.lista_dados

    def salvar(self):
            arquivo = open('Aula_23/exercicio/cadastro2.txt','a')    
            for dis in self.lista_dados:
                arquivo.write(f"{dis['Codigo']};{dis['Nome']};{dis['Idade']};{dis['Sexo']};{dis['Email']};{dis['Telefone']}\n")  
            arquivo.close()


    def consulta(self):
        codigo = int(input('Informe o codigo do cliente: '))
        for pessoa in self.lista_dados:
            if int(pessoa['Codigo']) == codigo:
                print(f"{pessoa['Codigo']};{pessoa['Nome']};{pessoa['Idade']};{pessoa['Sexo']};{pessoa['Email']};{pessoa['Telefone']}")
                break
            




cadastro = Cadastro()
cadastro.ler()
cadastro.consulta()
# cadastro.salvar()
# print(cadastro.ler())