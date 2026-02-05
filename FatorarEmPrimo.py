#Verifica de número é primo
def verifica_numero(numero):
    total = 0
    contador = 1
    while contador <= numero:
        if numero % contador == 0:
            total += 1
        contador += 1

    if total == 2:
        return True
    else:
        return False

# Retorna lista de todos os primos entre 1 e número
def listar_primos(numero):
    lista_de_primos = []
    for i in range(1, numero+1):
        if verifica_numero(i) == True: 
            lista_de_primos.append(i)
    return lista_de_primos

# Fatora um numero em números primos e mostra os números primos utilizados
def fatorar_numero(numero):
    #cria lista de primos desse numero
    lista = listar_primos(numero)
    resultado = []
    #divide o numero pelo primeiro da lista
    for i in lista:
        while numero % i == 0:
            numero = numero / i
            resultado.append(i)
    print(resultado)

# Relevar Fatores Primos de um número.
N = int(input("Digite um número: "))
fatorar_numero(N)



