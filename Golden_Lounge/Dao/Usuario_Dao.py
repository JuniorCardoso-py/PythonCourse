from Golden_Lounge.Dao.Base_Dao import Base_Dao
from Golden_Lounge.Model.Model_Pessoa import User


class Usuario_dao(Base_Dao):
    def __init__(self):
        super().__init__(User)