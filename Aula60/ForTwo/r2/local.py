
class Local:
    def __init__(self, lista:list):
        self.__pessoas = lista

    def entrada(self, pessoa:str):
        if self.valida_entrada(pessoa):
            self.__pessoas.append(pessoa)
            return True
        return False

    def saida(self, pessoa:str):
        if self.valida_saida(pessoa):
            self.__pessoas.remove(pessoa)
            return True
        elif pessoa == '':
            return True
        return False

    # valida saída de alguma pessoa do terminal
    def valida_saida(self, pessoa: str):

        if pessoa in self.__pessoas:
            if pessoa == 'policial' and 'presidiário' in self.__pessoas and len(self.__pessoas) > 2:
                return False
            if len(self.__pessoas) <= 4:
                # chefe de serviço - oficiais
                if pessoa == 'chefe de serviço' and 'piloto' in self.__pessoas and 'comissário1' in self.__pessoas and 'comissário2' in self.__pessoas:
                    return False
                    # piloto - comissários
                if pessoa == 'piloto' and 'chefe de serviço' in self.__pessoas and 'oficial1' in self.__pessoas and 'oficial2' in self.__pessoas:
                    return False
            if len(self.__pessoas) <= 3:
                # chefe de serviço - oficiais
                if pessoa == 'chefe de serviço' and 'piloto' in self.__pessoas and (
                        'comissário1' in self.__pessoas or 'comissário2' in self.__pessoas):
                    return False
                    # piloto - comissários
                if pessoa == 'piloto' and 'chefe de serviço' in self.__pessoas and (
                        'oficial1' in self.__pessoas or 'oficial2' in self.__pessoas):
                    return False
        else:
            return False
        return True

    def valida_entrada(self, pessoa):

        if len(self.__pessoas) <= 2:
            if len(self.__pessoas) == 1:
                if pessoa != 'policial' and 'presidiário' in self.__pessoas:
                    return False
                if pessoa == 'piloto' and ('comissário1' in self.__pessoas or 'comissário2' in self.__pessoas):
                    return False
                if pessoa == 'chefe de serviço' and ('oficial1' in self.__pessoas or 'oficial2' in self.__pessoas):
                    return False
            else:
                if pessoa == 'piloto' and 'comissário1' in self.__pessoas and 'comissário2' in self.__pessoas:
                    return False
                if pessoa == 'chefe de serviço' and 'oficial1' in self.__pessoas and 'oficial2' in self.__pessoas:
                    return False
        return True

    def get_pessoas(self)->str:
        lista_formatada = ''
        for p in self.__pessoas:
            lista_formatada = lista_formatada + f' {p} '
        return lista_formatada