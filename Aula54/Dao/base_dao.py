import sqlalchemy as db

class BaseDao:
    def __init__(self):
        conexao = db.create_engine("mysql+mysqlconnector://root:@localhost/novaaulabd")
        criador_sessao = db.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()