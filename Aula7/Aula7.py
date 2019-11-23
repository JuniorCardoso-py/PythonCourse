# Aula 7 14/11/2019.


lista = []
dicionario = {'chave':'valor', 'chave':'valor'}
dicionario = {'Nome':'Junior', 'Sobrenome':'Cardoso'}

print(dicionario)
print(dicionario['Sobrenome'])

nome = 'Junior'
lista_notas = [10,20,50,70]
media = sum(lista_notas) / len(lista_notas)
situacao = 'Reprovado'
if media >= 7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome':nome, 'lista_notas':lista_notas, 'Media':media, 'Situação':situacao}

print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situação']}")

