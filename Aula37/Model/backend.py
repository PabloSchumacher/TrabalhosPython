class Backend:
    idbackend = 0
    nome = ''

    def __str__(self):
        return f'{self.idbackend};{self.nome}'