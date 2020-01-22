class Sgbd:
    idsgbd = 0
    nome = ''

    def __str__(self):
        return f'{self.idsgbd};{self.nome}'