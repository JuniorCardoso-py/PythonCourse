#----- Exercicio 1 - Dicionario
#----- Escreva programa que leia os dados da cerveja
#----- Cerveja: Marca, tipo, IBU, ABV, EBC, Volume
#----- Crie um dicionario para armazenar os dados
#----- Imprima os dados do dicionario (não dicionario completo)

marca = input('Qual a marca da cerveja?: ')
tipo = input('Qual o tipo da cereveja?: ')
ibu = input('Qual o IBU?: ')
abv = input('Qual o ABV?: ')
ebc = input('Qual o EBC?: ')
vol = input('Qual o Volume?: ')

Cerveja = {'Marca':marca, 'Tipo':tipo, 'IBU':ibu,'ABV':abv, 'EBC':ebc, 'Volume':vol}

print(f"Marca:{Cerveja['Marca']} - \nTipo: {Cerveja['Tipo']} - \nIBU: {Cerveja['IBU']} - \nABV: {Cerveja['ABV']} ")
print(f" EBC: {Cerveja['EBC']} - \nVolume: {Cerveja['Volume']} ")

dicionario_bandas = {'Nome':''}
dicionario_bandas['Nome'] = 'Calipso'
dicionario_bandas['Nome'] = 'Dejavu'

print(dicionario_bandas)

dicionario = { 'Nome':'Maykon', 'Sobrenome':'Granemann' }
dicionario['Sobrenome'] = 'Rauen'
dicionario['CPF'] = '053.555.666-75'

print(dicionario)


