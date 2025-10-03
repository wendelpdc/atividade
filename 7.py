def fatorial(n):
    if n == 0:
        return 1  
    
    # Variável que guarda a multiplicação sequencial
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i       
    return resultado
try:
    num = int(input("Digite um número inteiro para calcular seu fatorial: "))
    if num < 0:
        print("Fatorial só é definido para números inteiros não-negativos.")
    else:
        print(f"\nO fatorial de {num} é: {fatorial(num)}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")