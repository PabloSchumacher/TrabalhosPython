import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select * from squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select * from squad where id = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" insert into squad
        (
            nome,
            descricao,
            npessoas,
            backend,
            frontend
        )
        values
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.npessoas},
            {squad.backend}
            {squad.frontend}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" update squad
        set
            nome = '{squad.nome}',
            descricao ='{squad.descricao}',
            npessoas = {squad.npessoas},
            backend = {squad.backend},
            frontend = {squad.frontend}
        where id = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from squad where id = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()