class Endereco:
    id = 0
    logradouro = ''
    numero = 0
    complemento = ''
    bairro = ''
    cidade = ''
    cep = 0

    def exportar_txt(self, lista_endereco):
        with open('Aula33/Aula33-4/endereco.txt','a') as arquivo:
            for e in lista_endereco:
                arquivo.write(f"{str(e)}\n")
    
    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'