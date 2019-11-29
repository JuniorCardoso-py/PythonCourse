marca  = input('Digite a marca da Cereveja: ')
teor = float(input('Digite o teor alcoolico da Cereveja : '))
litro = float(input('Digite a litragem da Cerveja : '))
dicionario = {'Marca':marca, 'Teor':teor, 'Litro':litro}

def dados(a):
    arquivo = open('Catalogo.txt', 'w')
    arquivo.write(f"Nome Da Cerveja: {dicionario['Marca']}\nO seu teor alcoolico: {dicionario['Teor']}%\nA sua litragem: {dicionario['Litro']}l")
    arquivo.close()

dados(dicionario)

def mostrar():
    arqui = open('Catalogo.txt', 'r')
    print(arqui)
    arqui.close()

mostrar()