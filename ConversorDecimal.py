# Conversão de Bases Numéricas
# Basicamente, da pra usar o resto da divisão para converter uma base em outra
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
# teste de commit

