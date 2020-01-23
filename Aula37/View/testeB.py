import sys
sys.path.append( r"C:\Users\900157\Documents\Github\TrabalhosPython\Aula37" )
from Controller.squad_controller import SquadController
from Model.squad import Squad

squad = Squad()
# squad.nome = 'SuperJooJ'
# squad.descricao = 'Profissional'
# squad.npessoas = 20
# squad.fk_backend = 2
# squad.fk_frontend = 2
# squad.fk_sgbd = 1
squad.id = 1

controller = SquadController()
print(controller.listar_todos())           #Buscando todos
#print(controller.buscar_por_id(squad))     #Buscando por id
#controller.deletar(3)                      #Deletando por id
#controller.salvar(squad)                   #Adicionando
#controller.alterar(squad)                   #Alterando 