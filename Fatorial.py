Numero = int(input("Digite um número para calcular o fatorial: "))
def fatorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	return result
	

print(f"O fatorial de {Numero} é {fatorial(Numero)}")
	