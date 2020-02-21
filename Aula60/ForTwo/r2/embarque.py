def embarque(motorista:str, passageiro:str, saida:dict):
    fortwo = {'motorista': motorista, 'passageiro': passageiro}
    saida['pessoas'].remove(motorista)
    print(f"{fortwo['motorista']} embarcou como motorista")

    if passageiro != '':
        saida['pessoas'].remove(passageiro)
        print(f"{fortwo['passageiro']} embarcou como passageiro")

    return fortwo