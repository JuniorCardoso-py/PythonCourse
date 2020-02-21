
from Aula60.ForTwo.r2.viagem import viagem, terminal, aviao

viagem('policial','presidiario', terminal, aviao)
viagem('policial','', aviao, terminal)
viagem('piloto','policial', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('piloto','oficial1', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('piloto','oficial2', terminal, aviao)
viagem('piloto','', aviao, terminal)
viagem('chefe de serviço','piloto', terminal, aviao)
viagem('chefe de serviço','', aviao, terminal)
viagem('chefe de serviço','comissário1', terminal, aviao)
viagem('chefe de serviço','', aviao, terminal)
viagem('chefe de serviço','comissário2', terminal, aviao)