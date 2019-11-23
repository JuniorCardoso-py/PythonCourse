#----- Exercicio 2 - Dicionarios
#----- Escreva programa que leia os dados de 11 jogadores
#----- Jogador: Nome, Posição, Numero, PernaBoa, 
#----- Crie um dicionario para armazenar os dados
#----- Imprima todos os jogadores e seus dados

jogadores = []



for i in range (1,3):
    nome = input(f'Qual o nome do Jogador {i} ?: ') 
    posi= input(f'Qual a posição do Jogador {i}? : ')
    num= input(f'Qual o numero da camiseta do Jogador {i}? : ')
    pb = input(f'Destrou ou Canhoto?{i} : ')
    jogadores.append(nome)
    jogadores.append(posi)
    jogadores.append(num)
    jogadores.append(pb)
jogadores = {'No':jogadores, 'Posi':jogadores,'Numero':jogadores,'pb':jogadores,}
print(f"'Nome do Jogador: {jogadores['No']} - Posição do Jogador: {jogadores['Posi']} - \nNumero:{jogadores['Numero']} - \nDestro ou Canhoto{jogadores['pb']}")