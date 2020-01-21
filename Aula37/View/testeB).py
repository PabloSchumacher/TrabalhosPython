import sys
sys.path.append(r'C:\Users\900157\Documents\Github\TrabalhosPython\Aula37')
from Controller.squad_controller import SquadController
from Model.squad import Squad

squad = Squad()
squad.nome = 'SuperJooJ'
squad.descricao = 'Profissional'
squad.npessoas = 10
squad.backend = 'Python'
squad.frontend = 'React'
squad.id = 1

controller = SquadController()
id_salvo = controller.salvar(squad)
pessoa_squad = controller.buscar_por_id(id_salvo)
print(controller.buscar_por_id(1))