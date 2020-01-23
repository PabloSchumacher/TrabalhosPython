import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.sgbd_controller import SgbdController
from Model.sgbd import Sgbd

sgbd = Sgbd()
sgbd.nome = 'Lua'
sgbd.idsgbd = 1

controller = SgbdController()
#print(controller.listar_todos())           #Buscando todos
#print(controller.buscar_por_id(sgbd))     #Buscando por id
controller.deletar(5)                      #Deletando por id
#controller.salvar(sgbd)                   #Adicionando
#controller.alterar(sgbd)                  #Alterando