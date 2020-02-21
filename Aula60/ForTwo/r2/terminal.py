from Aula60.ForTwo.r2.local import Local

class Terminal(Local):
    def __init__(self):
        self.__pessoas = [
                        'piloto', 'oficial1', 'oficial2'
                        ,'chefe de serviço', 'comissário1', 'comissário2'
                        ,'policial', 'presidiário'
                    ]

        super().__init__(self.__pessoas)

    def __str__(self):
        return 'Terminal'