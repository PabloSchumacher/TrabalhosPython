# Aula 22 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente:

    def __init__ (self,dadobruto):
        self.dadobruto = dadobruto.split(';')
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.atualizar(
            self.dadobruto[0],
            self.dadobruto[1],
            self.dadobruto[2],
            self.dadobruto[3],
            self.dadobruto[4],
            self.dadobruto[5],
        )

    def atualizar(self,codigo, nome, idade, sexo, email, telefone):
        self.codigo = int(codigo)
        self.nome = nome
        self.idade = int(idade)
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.dadobruto = f'{codigo};{nome};{idade};{sexo};{email};{telefone}'

    def imprime(self):
        print(f'Codigo do Cliente: {self.codigo}')
        print(f'Nome do Cliente: {self.nome}')
        print(f'Idade do Cliente: {self.idade}')
        print(f'Sexo do Cliente: {self.sexo}')
        print(f'Email do cliente: {self.email}')


cliente = Cliente(dadobruto)
cliente.imprime()
# cliente.atualizar(0,'',0,'','','')
# cliente.imprime()

def dados(codigo,nome,idade,sexo,email):
    dados = {'codigo':cliente.codigo, 'nome':cliente.nome, 'idade':cliente.idade, 'sexo':cliente.sexo, 'email':cliente.email, 'telefone':cliente.telefone}
    return dados

def salvar(dados):
    salvar = open('Aula23/exercicios/salvar.txt','a')
    salvar.write(f'{dados["codigo"]};{dados["nome"]};{dados["idade"]};{dados["sexo"]};{dados["email"]};{dados["telefone"]}\n')
    salvar.close()
    return salvar

dado = dados(0,'',29,'','')
salvar(dado)