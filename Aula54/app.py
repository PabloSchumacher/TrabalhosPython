from Aula55.dao.produto_dao import ProdutoDao
dao = ProdutoDao()
produtos = dao.listar_todos()
print(produtos)
for p in produtos:
    print(p)

print("-"*10)
print(dao.buscar_por_id(1))