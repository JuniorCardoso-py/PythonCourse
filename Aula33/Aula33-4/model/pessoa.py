class Pessoa:
    id = 0
    nome = ''
    sobrenome = ''
    idade = 0
    endereco_id = 0

    def exportar_txt(self, lista_pessoas):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('Aula33/Aula33-4/pessoas4.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco_id}'