while True:
    numero = int(input("Digite um número: "))
    total = 0
    contador = 1
    while contador <= numero:
        if numero % contador == 0:
            total += 1
        contador += 1

    if total == 2:
        print("Número é primo")
    else:
        print("Número não é primo")