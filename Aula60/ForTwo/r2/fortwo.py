from Aula60.ForTwo.r2.local import Local
class Fortwo:
    def __init__(self):
        self.__pessoas_permitidas = ['piloto', 'chefe de serviço','policial']
        self.__motorista = ''
        self.__passageiro = ''

    def set_motorista(self, pessoa):
        if pessoa in self.__pessoas_permitidas:
            self.__motorista = pessoa
            return True
        return False

    def get_motorista(self):
        return self.__motorista

    def set_passageiro(self, pessoa):
       if self.__valida_regra_passageiro__(pessoa):
            self.__passageiro = pessoa
            return True
       return False

    def get_passageiro(self):
        return self.__passageiro

    def __valida_regra_passageiro__(self, pessoa) -> bool:
        if self.__motorista == 'policial':
            if self.__passageiro == 'presidiário' or self.__passageiro == '':
                return True
        elif self.__motorista == 'piloto':
            if pessoa != 'comissário1' and pessoa != 'comissário2' and pessoa != 'presidiário' and pessoa == '':
                return True
        elif self.__motorista == 'chefe de serviço':
            if pessoa != 'oficial1' and pessoa != 'oficial2' or pessoa != 'presidiário' and pessoa == '':
                return True
        return False

    def viagem(self, origem:Local, destino):
        print(f"Saindo do {origem}")
        print('Iniciando a viagem...')
        print(f'motorista: {self.__motorista} passageiro: {self.__passageiro}')
        print(f"Chegando no {destino}")
        print('Finalizando a viagem ...')
        print(f'{self.__motorista} e {self.__passageiro} descem no {destino}')
        print(f'origem: {origem.get_pessoas()}')
        print(f'destino: {destino.get_pessoas()}')




