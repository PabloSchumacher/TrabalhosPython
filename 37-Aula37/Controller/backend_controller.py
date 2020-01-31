from Dao.backend_dao import BackendDao
from Model.backend import *

class BackendController:
    dao = BackendDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, backend:Backend):
        return self.dao.salvar(backend)

    def alterar(self, backend:Backend):
        self.dao.alterar(backend)

    def deletar(self, id):
        self.dao.deletar(id)
