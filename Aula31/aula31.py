#Banco de Dados
#SGBD
# Mysql, SqlServer

#Mysql -MariaDb

# CRUD
# C = CREAT - INSERT/SALVAR     - Insert
# R = READ - LER/LISTAR         - Select
# U = UPDATE - ALTERAR
# D = DELETE - APAGAR

import MySQLdb

#Listando Todos dados da tabela
def listar_todos(c):
    c.execute('select * FROM tb_pessoa')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)

#Buscar por Id
def buscar_por_id(c, id):
    c.execute(f'select * FROM tb_pessoa WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)
#Buscar por Sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"select * FROM tb_pessoa WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

conexao = MySQLdb.connect(host='localhost', database='aula_bd', user='root', passwd='')
cursor= conexao.cursor()

#listar_todos(cursor)
# buscar_por_id(cursor, 3)
#buscar_por_sobrenome(cursor,'Sil')

#Salvar Pessoa
def salvar(cn,cr,Nome,SobreNome,Idade, endereco_id=None):
    if endereco_id == None:
        endereco_id = 'NULL'
    cr.execute(f"insert into tb_pessoa (Nome,SobreNome,Idade,endereco_id) VALUES ('{Nome}', '{SobreNome}' , {Idade} , {endereco_id} ) ")
    cn.commit()

salvar(conexao,cursor,'Pablo','Cardoso',12,2)