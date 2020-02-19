from Golden_Lounge.Model.Model_Pessoa import Tabela_das_pessoas
from Golden_Lounge.Dao.Base_Dao import Base_Dao

class Pessoas_Dao(Base_Dao):
    def __init__(self):
        super().__init__(Tabela_das_pessoas)