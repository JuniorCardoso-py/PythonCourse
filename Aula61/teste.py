def binary_gap(numero):
    numero = bin(numero)
    print(numero)
    numero = numero[2:]
    print(numero)
    numero = str(numero)
    print(type(numero))
    numero = numero.strip('0').split('1')
    print(numero)
    return len(max(numero))

print(binary_gap(35))
print(bin(35)[2:])