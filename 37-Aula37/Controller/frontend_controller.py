from Dao.frontend_dao import FrontendDao
from Model.frontend import *

class FrontendController:
    dao = FrontendDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, frontend:Frontend):
        return self.dao.salvar(frontend)

    def alterar(self, frontend:Frontend):
        self.dao.alterar(frontend)

    def deletar(self, id):
        self.dao.deletar(id)
