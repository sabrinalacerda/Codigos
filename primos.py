def eh_primo(n):
    for d in range(2, n//2 + 1):
        if n % d == 0:
            return False
        return True

numero = int(input("Digite: "))
eh_primo(numero)