# Aula 18 - 03-11-2019

# Ao receber a seguinte lista, faça um metodo que retorne cada um destes itens de forma individual 
# com cabaçalho dizendo em que posição estes itens estão dentro da lista principal:
# Exemplo: 
# ############# posição 0 ##################
# Agua
# mamão
# ############# posição 1 ##################
# banana
# limão

#Regra: Não pode usar a função range e no máximo 2 print()

lista = [
          ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'], #0
          ['skol','kaiser','sol','schin','brahma','itaipava','bavaria'], #1
          ['alface crespa', 'alface lisa','rucula','almerão','repolho','salsinha',], #2
          ['rizoto','macarronada','polenta','guizado','dobradinha','revirado','pure'], #3
          ['feijão', 'erviha', 'lentilha','vagem','feijão branco','gão de bico','soja'], #4
          ['agua','cachoeira','rio','lagoa','sanga','brejo','laguna'], #5
          ['vento','ciclone','tufão','furacão','brisa','minuano','zefiro'], #6
          ['carro','moto','vespa','caminhão','sprinter','kombi','fusca'], #7
          ['calça','camisa','japona','jaqueta','camiseta','bone','regata'] #8
        ]

cont=0
for a in lista:
  print(f'\n ############# posição {cont} ################## \n')
  cont=cont+1
  for b in a:
    print(b)