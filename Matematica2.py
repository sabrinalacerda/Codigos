# Conversão de Bases Numéricas
def de_decimal (n, base):
    # quociente
    quociente = n
    numero = []
    while quociente >= base:
        resto = quociente % base
        numero.insert(0, int(resto))
        quociente = quociente / base
    numero.insert(0, int(quociente))
    print (numero)

    # print list
usuario = input("Coloque um numero: ")
de_decimal (int(usuario), 16)
