# Pedra, Papel e Tesoura


jogador1 = int(input("Pedra[0], Papel[1] ou Tesoura[2]? "))
jogador2 = int(input("Pedra[0], Papel[1] ou Tesoura[2]? "))

if jogador1 == jogador2:
    print ("Empate!")
elif jogador1 == (jogador2 + 1)%3:
    print ("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")
