import MySQLdb

def listar_todosend(c):
    c.execute('select * from endereco')
    endereco = c.fetchall()
    for e  in  endereco:
        print(e)

def buscar_por_id(c, idendereco):
    c.execute(f'select * from endereco where idendereco = {idendereco}')
    endereco = c.fetchall()
    print(endereco)

def buscar_por_cep(c, cep):
    c.execute(f'select * from endereco where cep = {cep}')
    for e  in  c.fetchall():
        print(e)

def salvar_endereco(cn, cr, pais, estado, cidade, rua, numero, complemento, cep):
    cr.execute(f"insert into endereco (pais, estado, cidade, rua, numero, complemento, cep) values('{pais}', '{estado}','{cidade}','{rua}',{numero},'{complemento}',{cep})")
    cn.commit()

def alterar_endereco(cn, cr, idendereco, pais, estado, cidade, rua, numero, complemento, cep):
    cr.execute(f"update endereco set pais='{pais}', estado='{estado}', cidade='{cidade}', rua='{rua}', numero={numero}, complemento='{complemento}', cep={cep} where idendereco={idendereco}")
    cn.commit()

def deletar_endereco(cn, cr, idendereco):
    cr.execute(f"delete from endereco where idendereco={idendereco}")
    cn.commit()

conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
cursor = conexao.cursor()

listar_todosend(cursor)
#buscar_por_id(cursor, 1)
#buscar_por_cep(cursor, 89058000)
#salvar_endereco(conexao,cursor,'Brasil','Santa Catarina','Blumenau','Rua JooJ',45,'Casa',89053130)
#alterar_endereco(conexao,cursor,3,'Brasil','Santa Catarina','Blumenau','Rua Cavalinho',35,'Ap 12',89050250)
#deletar_endereco(conexao, cursor, 2)