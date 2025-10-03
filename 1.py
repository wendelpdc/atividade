valor_produto = float(input("Digite o valor do produto: R$ "))

desconto = valor_produto * 0.10
valor_produto -= desconto

print(f"O valor do desconto foi de: R$ {desconto:.2f}")
print(f"O valor final da compra com 10% de desconto é: R$ {valor_produto:.2f}")