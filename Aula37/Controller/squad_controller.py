from Dao.squad_dao import SquadDao
from Model.squad import *
from Controller.backend_controller import BackendController
from Controller.frontend_controller import FrontendController
from Controller.sgbd_controller import SgbdController

class SquadController:
    dao = SquadDao()
    be = BackendController()
    fro = FrontendController()
    bd = SgbdController()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, squad:Squad):
        squad.backend.idbackend = self.be.salvar(squad.backend)
        squad.frontend.idfrontend = self.fro.salvar(squad.frontend)
        squad.sgbd.idsgbd = self.bd.salvar(squad.sgbd)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)
