import MySQLdb
from Model.sgbd import Sgbd

class SgbdDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans08', user='padawans08', passwd='kp2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select * from sgbd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select * from sgbd where idsgbd = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbd:Sgbd):
        comando = f""" insert into sgbd
        (
            nome
        )
        values
        (
            '{sgbd.nome}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgbd:Sgbd):
        comando = f""" update sgbd
        set
            nome = '{sgbd.nome}'
        where idsgbd = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from sgbd where idsgbd = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()