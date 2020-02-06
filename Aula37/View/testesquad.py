import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.squad_controller import SquadController
from Model.squad import Squad

squad = Squad()
squad.nome = 'JooJ'
squad.descricao = 'Intermediário'
squad.npessoas = 20
squad.backend.nome = 'Lua'          #Adicionar
squad.backend.idbackend = 1         #Alterar
squad.frontend.nome = 'Lua'         #Adicionar
squad.frontend.idfrontend = 1       #Alterar
squad.sgbd.nome = 'Lua'             #Adicionar
squad.sgbd.idsgbd = 1               #Alterar
squad.id = 6

controller = SquadController()
#controller.deletar(5)                      #Deletando por id
#controller.salvar(squad)                   #Adicionando
controller.alterar(squad)                   #Alterando
print(controller.listar_todos())           #Buscando todos
#print(controller.buscar_por_id(squad))     #Buscando por id