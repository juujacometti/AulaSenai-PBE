#  Solicite ao usuário uma nota entre 0 e 10 e classifique-a: A (9 a 10), B (7 a 8), C (5 a 6), D (3 a 4), E (0 a 2).

nota = float(input("Digite a nota do aluno:\n"))

if (nota >= 0 and nota < 3):
    print("Você tirou nota E")
    
elif (nota >= 3 and nota < 5):
    print("Você tirou nota D")
    
elif (nota >= 5 and nota < 7):
    print("Você tirou nota C")
    
elif (nota >= 7 and nota < 9):
    print("Você tirou nota B")
    
else:
    print("Você tirou nota A") 
