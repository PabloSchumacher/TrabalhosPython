import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.squad_controller import SquadController
from Model.squad import Squad

squad = Squad()
squad.nome = 'JooJ'
squad.descricao = 'Intermediário'
squad.npessoas = 20
squad.backend.nome = 'Lua'
squad.frontend.nome = 'Lua'
squad.sgbd.nome = 'Lua'
squad.id = 6

controller = SquadController()
#controller.deletar(5)                      #Deletando por id
#controller.salvar(squad)                   #Adicionando
controller.alterar(squad)                   #Alterando
print(controller.listar_todos())           #Buscando todos
#print(controller.buscar_por_id(squad))     #Buscando por id