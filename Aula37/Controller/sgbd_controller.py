import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Dao.sgbd_dao import SgbdDao
from Model.sgbd import *

class SgbdController:
    dao = SgbdDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, sgbd:Sgbd):
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:Sgbd):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)
