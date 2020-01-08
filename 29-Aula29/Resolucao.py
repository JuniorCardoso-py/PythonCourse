# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.
# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python
from time import sleep
print('#'*10, 'HBSIS AIRLINES', '#'*10)
aviao = []
terminal = ['Piloto','Oficial 1','Oficial 2','Chefe de Voo','Comissaria 1','Comissaria 2','Policial','Presidiario']
def status():
    sleep(2)
    print(f'\nSobraram no terminal os seguintes passageiros: {terminal}')
    sleep(2)
    print(f'\nNo avião estão o seguintes passageiros: {aviao}')
    sleep(2)
def embarque_e(policial,piloto):
    print(f'\nEmbarcaram no ForTwo o {policial} e o {piloto}.')
    aviao.append(piloto)
    aviao.append(policial)
    terminal.remove(policial)
    terminal.remove(piloto)
def embarque_for_two(mot, pas):
    print(f'\nEmbarcaram no ForTwo o {mot} e o {pas}.')
    terminal.remove(mot)
    terminal.remove(pas)
    aviao.append(pas)
    print(f'\nO {mot} volta para o terminal para a proxima viagem.')
    terminal.append(mot)
def adic_terminal(passageiro):
    terminal.append(passageiro)
    aviao.remove(passageiro)
    print(f'\nO {passageiro} volta para o terminal para a proxima viagem.')
def adic_aviao(passageiro1):
    terminal.remove(passageiro1)
    aviao.append(passageiro1)
def solucao_exercicio():
    sleep(2)
    print('\nO automovel partiu ao destino para buscar passageiros.')
    sleep(2)
    #========== viagem 1
    embarque_for_two('Piloto','Oficial 1')
    status()
    #========== viagem 2
    embarque_for_two('Chefe de Voo','Comissaria 1')
    status()
    #========== viagem 3
    embarque_for_two('Piloto','Oficial 2')
    status()
    #========== viagem 4
    embarque_for_two('Chefe de Voo','Piloto')
    status()
    #========== viagem 5
    embarque_for_two('Chefe de Voo','Comissaria 2')
    status()
    #========== viagem 6
    embarque_e('Policial','Presidiario')
    status()
    adic_terminal('Piloto')
    #========== viagem 7
    embarque_for_two('Piloto','Chefe de Voo')
    adic_aviao('Piloto')
    status()
solucao_exercicio()