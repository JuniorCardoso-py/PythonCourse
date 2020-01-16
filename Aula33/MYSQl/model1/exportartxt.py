from Aula33.MYSQl.dao1.database import Tratamento
class Exportar:
    def importar_arquivo(self,lista_tuplas):
        with open('../view1/Endereco.txt', 'w') as arquivo:
            for p in Tratamento:
                arquivo.write(f"{p['Logradouro'],}, {p['Numero']}, {p['Complemento']}, {p['Bairro']},{p['Cidade']}, {p['Endereco']}\n")
