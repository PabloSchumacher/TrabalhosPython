from Model.backend import Backend
from Model.frontend import Frontend
from Model.sgbd import Sgbd
class Squad:
    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao = ''
        self.npessoas = 0
        self.backend = Backend()
        self.frontend = Frontend()
        self.sgbd = Sgbd()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.npessoas};{self.backend.idbackend};{self.frontend.idfrontend};{self.sgbd.idsgbd}'