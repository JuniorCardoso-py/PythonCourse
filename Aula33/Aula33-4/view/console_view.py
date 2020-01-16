import sys
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)