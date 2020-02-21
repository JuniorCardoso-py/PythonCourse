from Aula60.ForTwo.r2.embarque import embarque
from Aula60.ForTwo.r2.desembarque import desembarque

from Aula60.ForTwo.r2.terminal import Terminal
from Aula60.ForTwo.r2.aviao import Aviao
from Aula60.ForTwo.r2.local import Local
from Aula60.ForTwo.r2.fortwo import Fortwo


def viagem(motorista:str, passageiro:str):
    terminal = {'descricao':'terminal', 'pessoas': ['piloto','oficial1','oficial2','chefe de serviço','comissário1','comissário2','policial','presidiario']}
    aviao = { 'descricao':'aviao', 'pessoas': [] }
    fortwo = embarque(motorista, passageiro, terminal)
    print(f"Saindo do {terminal['descricao']}")
    print('Iniciando a viagem...')
    print(f"Chegando no {aviao['descricao']}")
    print('Finalizando a viagem ...')
    # alto acoplamento
    desembarque(fortwo, aviao)
    print(terminal['pessoas'])
    print(aviao['pessoas'])

def viagem2(pessoa1, pessoa2, origem:Local, destino:Local):
    fortwo = Fortwo()
    origem.entrada(pessoa1)
    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            origem.entrada(pessoa2)
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa1):
                        if not destino.entrada(pessoa2):
                            print('Não permitido6')
                    else:
                        print('Não permitido5')
                else:
                    print('Não permitido4')
            else:
                print('Não permitido3')
        else:
            print('Não permitido2')
    else:
        print('Não permitido1')


print('Viagem 1')
viagem2('policial','presidiário', Terminal(), Aviao())
print('Viagem 2')
viagem2('policial','', Aviao(), Terminal())
print('Viagem 3')
viagem2('piloto','policial', Terminal(), Aviao())
print('Viagem 4')
viagem2('piloto','', Aviao(), Terminal())
print('Viagem 5')
viagem2('piloto','oficial1', Terminal(), Aviao())
print('Viagem 6')
viagem2('piloto','', Aviao(), Terminal())
print('Viagem 7')
viagem2('piloto','oficial2', Terminal(), Aviao())
print('Viagem 8')
viagem2('piloto','', Aviao(), Terminal())
print('Viagem 9')
viagem2('chefe de serviço','piloto', Terminal(), Aviao())
print('Viagem 10')
viagem2('chefe de serviço','', Aviao(), Terminal())
print('Viagem 11')
viagem2('chefe de serviço','comissário1', Terminal(), Aviao())
print('Viagem 12')
viagem2('chefe de serviço','', Aviao(), Terminal())
print('Viagem 13')
viagem2('chefe de serviço','comissário2', Terminal(), Aviao())
print('Viagem Final')