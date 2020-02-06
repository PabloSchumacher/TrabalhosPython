import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.frontend_controller import FrontendController
from Model.frontend import Frontend

frontend = Frontend()
frontend.nome = 'JavaScript'
frontend.idfrontend = 5

controller = FrontendController()
print(controller.listar_todos())           #Buscando todos
#print(controller.buscar_por_id(frontend))     #Buscando por id
#controller.deletar(4)                      #Deletando por id
#controller.salvar(frontend)                   #Adicionando
#controller.alterar(frontend)                   #Alterando 