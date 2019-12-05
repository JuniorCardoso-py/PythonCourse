# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

cabe = cerveja[0] # Aqui ele vai separar da seguinte forma
 # ('marca', 'tipo', 'ibu','preço')

dados = cerveja [1:] # Aqui separa dessa forma 
#          ('Skol','IPA','ultra-leve',3.50),  # Para cada elemento dentro da tupla é contado por posição 0,1,2,3.
#          ('Brahma','lager','leve/media',3.45),
#          ('Kaiser','Americam Larger','leve',2.35),
#          ('Sol','larger mão','agua',1.19)


for dados_cerveja in dados: # para cada elemento ou nesse caso para cada tupla na variavel dados vai adicionar as tuplas separadas
    print(dados_cerveja) # esse eu coloquei só para ver como fica
    print(f'\n{cabe[0]} - {dados_cerveja[0]}')
    print(f'\n{cabe[1]} - {dados_cerveja[1]}')
    print(f'\n{cabe[2]} - {dados_cerveja[2]}')
    print(f'\n{cabe[3]} - {dados_cerveja[3]}')

for dados_cerveja in dados:
    for i in range(4):
        print(f'\n{cabe[i]} - {dados_cerveja[i]}')

