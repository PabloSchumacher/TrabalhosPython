# Aula 23 - 10-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (_init_) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Cliente:

    def __init__ (self,dadobruto):
        self.dadobruto = dadobruto.split(';')
        self.codigo = None
        self.nome = None
        self.idade = None
        self.sexo = None
        self.email = None
        self.telefone = None
        self.adicionar(
            self.dadobruto[0],
            self.dadobruto[1],
            self.dadobruto[2],
            self.dadobruto[3],
            self.dadobruto[4],
            self.dadobruto[5],
        )

    def adicionar(self,codigo, nome, idade, sexo, email, telefone):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone

cliente = Cliente(dadobruto)
print(f'Codigo do Cliente: {cliente.codigo}')
print(f'Nome do Cliente: {cliente.nome}')
print(f'Idade do Cliente: {cliente.idade}')
print(f'Sexo do Cliente: {cliente.sexo}')
print(f'Email do cliente: {cliente.email}')