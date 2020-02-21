
def desembarque(fortwo:dict, chegada:dict):
    print(f"{fortwo['motorista']} desembarcou")
    chegada['pessoas'].append(fortwo['motorista'])
    fortwo['motorista'] = ''

    if fortwo['passageiro'] != '':
        print(f"{fortwo['passageiro']} desembarcou")
        chegada['pessoas'].append(fortwo['passageiro'])
        fortwo['passageiro'] = ''