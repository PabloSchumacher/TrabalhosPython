import MySQLdb
from Model.sgbd import Sgbd

class SgbdDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select * from sgbd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select * from sgbd where id = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
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

    def alterar(self, squad:Squad):
        comando = f""" update sgbd
        set
            nome = '{sgbd.nome}'
        where id = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from sgbd where id = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()