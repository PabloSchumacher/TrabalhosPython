import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.backend_controller import BackendController
from Model.backend import Backend

backend = Backend()
backend.nome = 'Python'
backend.idbackend = 7

controller = BackendController()
#controller.deletar(7)                        #Deletando por id
#controller.salvar(backend)                   #Adicionando
#controller.alterar(backend)                   #Alterando 
#print(controller.listar_todos())             #Buscando todos
#print(controller.buscar_por_id(backend))     #Buscando por id