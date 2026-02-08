# Pedra, Papel e Tesoura
# Utilizamos o resto da divisão para fechar um ciclo de opções
while True:
    jogador1 = int(input("Jogador1: "))
    jogador2 = int(input("Jogador2: "))

    resultado1 = (jogador2+1)%5
    resultado2 = (jogador2+3)%5

    # Compara o input dos dois jogadores
    if jogador1 == jogador2:
        print ("Empate!")
    # Ponto chave: Se jogador 2 escolher tesoura e Jogador 1 escolher pedra, diminuímos o valor de tesoura para que pedra ganhe
    # Usando resto da divisão
    elif jogador1 == resultado1 or jogador1 == resultado2:
        print(jogador1, "é igual a", resultado1, "ou", resultado2)
        print ("Jogador 1 venceu!")
    else:
        print(jogador1, "é diferente de", resultado1, "e", resultado2)
        print("Jogador 2 venceu!")
