# pip3 install flask_mysqldb
# referencia ao Mysql

import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('select * from pessoas')
    pessoas = c.fetchall()
    for p  in  pessoas:
        print(p)
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'select * from pessoas where id = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"select * from pessoas where sobrenome like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, nascimento, endereco_id='NULL'):
    cr.execute(f"insert into pessoas (nome, sobrenome, nascimento, endereco_id) values('{nome}', '{sobrenome}',{nascimento},{endereco_id})")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, nascimento, endereco_id='NULL'):
    cr.execute(f"update pessoas set nome='{nome}', sobrenome='{sobrenome}', nascimento='{nascimento}', endereco_id={endereco_id} where id={id} ")
    cn.commit()

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'delete from pessoas where id={id}')
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

#listar_todos(cursor)
#buscar_por_id(cursor, 1)
#buscar_por_sobrenome(cursor,'Schu')
#salvar(conexao, cursor, 'Voltolini', 'KingOfFlask', '1999-01-08',1)
alterar(conexao, cursor, 12, 'Gugu Voltolini', 'KingOfBasquete', '2002-08-11', 1)
#deletar(conexao, cursor, 1)