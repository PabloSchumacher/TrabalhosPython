import MySQLdb
from Model.backend import Backend

class BackendDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans08', user='padawans08', passwd='kp2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select * from backend"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select * from backend where idbackend = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, backend:Backend):
        comando = f""" insert into backend
        (
            nome
        )
        values
        (
            '{backend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, backend:Backend):
        comando = f""" update backend
        set
            nome = '{backend.nome}'
        where idbackend = {backend.idbackend}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from backend where idbackend = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()