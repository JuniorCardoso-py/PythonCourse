
from model.pessoa import Pessoa
from dao.pessoa_db import PessoaDb

class PessoaController:
    p = Pessoa()
    p_db = PessoaDb()

    def listar_todos(self):
        return self.p_db.listar_todos()

    def exportar(self):
        lpc = self.p_db.listar_todos()
        self.p.exportar_txt(lpc)
