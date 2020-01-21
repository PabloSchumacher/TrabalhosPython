class Squad:
    id = 0
    nome = ''
    descricao = ''
    npessoas = 0
    backend = ''
    frontend = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.npessoas};{self.backend};{self.frontend}'