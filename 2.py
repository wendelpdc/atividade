

print("Compare dois número inteiros para saber se é maior, menor ou igual.")      
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    print(f"{a} é maior que {b}.")
elif a < b:
    print(f"{b} é maior que {a}.")
elif a == b:
    print("São número iguais.")
else:
    print("Erro, tente novamente.")
    
    
    