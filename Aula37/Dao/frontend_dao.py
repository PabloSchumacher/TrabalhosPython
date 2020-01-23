import MySQLdb
from Model.frontend import Frontend

class FrontendDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans08', user='padawans08', passwd='kp2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select * from frontend"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select * from frontend where id = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, frontend:Frontend):
        comando = f""" insert into frontend
        (
            nome
        )
        values
        (
            '{frontend.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, frontend:Frontend):
        comando = f""" update frontend
        set
            nome = '{frontend.nome}'
        where id = {frontend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from frontend where id = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()