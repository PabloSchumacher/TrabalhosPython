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

conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')

def listar_todos(c):
    c.execute('select * from pessoas')
    pessoas = c.fetchall()
    for p in pessoas:
        print (p)

def buscar_por_id(c,id):
    c.execute(f'select * from pessoas where id = {id}')
    pessoas = c.fetchone()
    print(pessoas)

conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
cursor=conexao.cursor()

buscar_por_id(cursor,1)