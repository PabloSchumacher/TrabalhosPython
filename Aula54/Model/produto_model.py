import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()
class ProdutoModel(BaseAlchemy):
    __tablename__ = "Produto"
    idproduto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=45))

    def __str__(self):
        return f"{self.idproduto}-{self.nome}"

    def __repr__(self):
        return self.__str__()