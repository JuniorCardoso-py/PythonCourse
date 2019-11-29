#Aula 15 - 28/11/2019
#Manipulação de arquivos.

arquivo = open('aula15.txt','a')
arquivo.write('Voltolini Turismo\n')
arquivo.close

arquivo = open('aula15.txt','a')
for linha in arquivo:
    print(linha)
arquivo.close()


#----Modo mais correto---- Usando Input
n1 = input('Digite seu nome: ')
arquivo = open('aula15.1.txt','a')
arquivo.write(f'{n1}\n')
arquivo.close()

#ou

arquivo = open('aula15.1.txt','a')
arquivo.write(f"{input('Digite seu nome: ')}\n")
arquivo.close()

