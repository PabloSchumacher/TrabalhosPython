from Model.backend import Backend
from Model.frontend import Frontend
from Model.sgbd import Sgbd
class Squad:
    id = 0
    nome = ''
    descricao = ''
    npessoas = 0
    backend = Backend()
    frontend = Frontend()
    sgbd = Sgbd()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.npessoas};{self.backend.idbackend};{self.frontend.idfrontend};{self.sgbd.idsgbd}'