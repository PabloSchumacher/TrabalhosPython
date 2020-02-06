from Aula54.Dao.base_dao import BaseDao
from Aula54.Model.produto_model import ProdutoModel

class ProdutoDao(BaseDao):
    def list_all(self):
        return self.sessao.query(ProdutoModel).all()