try:
    num_limite = int(input("Digite um número inteiro positivo (limite): "))
    if num_limite < 0:
        print("O número deve ser positivo. Por favor, tente novamente.")
        
except ValueError:
    print("Entrada inválida. Digite um número inteiro.")

print(f"\nNúmeros pares de 0 até {num_limite}:")
for num in range(num_limite + 1):
    if num % 2 == 0:
        print(num)