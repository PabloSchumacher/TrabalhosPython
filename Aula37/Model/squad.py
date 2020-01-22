class Squad:
    id = 0
    nome = ''
    descricao = ''
    npessoas = 0
    fk_backend = 0
    fk_frontend = 0
    fk_sgbd = 0

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.npessoas};{self.fk_backend};{self.fk_frontend};{self.fk_sgbd}'