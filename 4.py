def verif_duplicatas(lista):
    conjunto = set(lista)
    
    if len(lista) != len(conjunto):
        return "A lista possui valores duplicados."
    else:
        return "A lista NÃO possui valores duplicados."
    
    
list = [10, "apple", 20, 11, "banana", "maçã"]
print(f"Valores da lista: {list}")
print(verif_duplicatas(list)) 