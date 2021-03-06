import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.padawans.dev', database='padawans08', user='padawans08', passwd='kp2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"select id, s.nome, descricao, npessoas, b.nome, f.nome, g.nome from squad as s join backend as b on s.fk_backend = b.idbackend join frontend as f on s.fk_frontend = f.idfrontend join sgbd as g on s.fk_sgbd = g.idsgbd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"select id, s.nome, descricao, npessoas, b.nome, f.nome, g.nome from squad as s join backend as b on s.fk_backend = b.idbackend join frontend as f on s.fk_frontend = f.idfrontend join sgbd as g on s.fk_sgbd = g.idsgbd where id = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" insert into squad
        (
            nome,
            descricao,
            npessoas,
            fk_backend,
            fk_frontend,
            fk_sgbd
        )
        values
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.npessoas},
            {squad.backend.idbackend},
            {squad.frontend.idfrontend},
            {squad.sgbd.idsgbd}
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
            fk_backend = {squad.backend.idbackend},
            fk_frontend = {squad.frontend.idfrontend},
            fk_sgbd = {squad.sgbd.idsgbd}
        where id = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"delete from squad where id = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()