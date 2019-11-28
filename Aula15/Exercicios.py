marca  = input('Digite a marca da Cereveja: ')
teor = float(input('Digite o teor alcoolico da Cereveja : '))
litro = float(input('Digite a litragem da Cerveja : '))
dicionario = {'Marca':marca, 'Teor':teor, 'Litro':litro}

def dados(a):
    a = dicionario
    arquivo = open('Catalogo.txt', 'a')
    arquivo.write(f'{a['Marca']} - {a['Teor']} - {a['Litro']}')
    arquivo.close()

dados(dicionario)