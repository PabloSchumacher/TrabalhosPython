from Aula54.Dao.base_dao import BaseDao
from Aula54.Model.produto_model import ProdutoModel

class ProdutoDao(BaseDao):
    def listar_todos(self):
        return self.sessao.query(ProdutoModel).all()
    def buscar_por_id(self,id):
        return self.sessao.query(ProdutoModel).filter_by(id=id).one()
    def deletar(self,id):
        model = self.sessao.query(ProdutoModel).filter_by(id=id).one()
        self.sessao.commit()
        self.sessao.deletar(model)
        return f"Deletado objeto de id {id}"
    def inserir(self,ProdutoModel):
        self.sessao.add(model)
        self.sessao.commit()
        return f"Produto de {model.id} criada"
    def alterar(self, ProdutoModel):
        self.sessao.merge(model)
        self.sessao.commit()
        return f"Produto {model.nome} alterada com sucesso"