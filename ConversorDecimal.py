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

# Converte base decial para qualquer outra base
usuario = input("Coloque um numero: ")
de_decimal (int(usuario), 16)

