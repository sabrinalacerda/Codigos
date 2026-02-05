# Pedra, Papel e Tesoura
# Utilizamos o resto da divisão para fechar um ciclo de opções

jogador1 = int(input("Pedra[0], Papel[1] ou Tesoura[2]? "))
jogador2 = int(input("Pedra[0], Papel[1] ou Tesoura[2]? "))

# Compara o input dos dois jogadores
if jogador1 == jogador2:
    print ("Empate!")
# Ponto chave: Se jogador 2 escolher tesoura e Jogador 1 escolher pedra, diminuímos o valor de tesoura para que pedra ganhe
# Usando resto da divisão
elif jogador1 == (jogador2 + 1)%3:
    print ("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")
