
def mario_pyramid(Altura):
    for Contador in range(Altura):
        for Espacos in range(Altura - Contador - 1):
            print(" ", end="");
        for Blocos in range(Contador + 1):
            print("#", end="");
        print("");

Altura = int(input("Digite a altura da pirâmide: "))
mario_pyramid(Altura);

frutas = ["maçã", "banana", "cereja"]

# Loop X (fruta) em Y (frutas)
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

    # Loop de 0 a 4 (de X a Y, onde Y é exclusivo)
for numero in range(2, 5):
    print(f"Número atual: {numero}")

