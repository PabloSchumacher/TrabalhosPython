
from Aula54.Dao.produto_dao import ProdutoDao
dao = ProdutoDao()
produtos = dao.list_all()
print(produtos)
for p in produtos:
    print(p)