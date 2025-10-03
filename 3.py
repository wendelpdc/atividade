def avaliar_idade():
    idade = int(input("Digite uma idade para saber se é criança, adolescente, adulto ou idoso: "))
    
    if idade < 12:
        print("Criança.")
    elif idade >= 12 and idade <= 17:
        print("Adolescente.")
    elif idade >= 18 and idade <= 64:
        print("Adulto.")
    elif idade >= 65:
        print("Idoso.")
    else:
        print("Idade inválida.")
        
    return avaliar_idade()
         

print(avaliar_idade())