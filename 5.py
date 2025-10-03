try:
    ano = int(input("Digite um ano para verificar se ele é bissexto: "))
except ValueError:
    print("Entrada inválida. Digite um número inteiro para o ano.")
    
ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if ano_bissexto:
    print(f"\nO ano {ano} É bissexto.")
else:
    print(f"\nO ano {ano} NÃO é bissexto.")