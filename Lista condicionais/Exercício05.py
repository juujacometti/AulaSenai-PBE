# Pergunte ao usuário para inserir um número e diga se é positivo, negativo ou zero

numero = float(input("Digite um número:\n"))

if numero > 0:
    print(f"O número {numero} é positivo.")

elif numero == 0:
    print(f"O número digitado foi zero.")

else:
    print(f"O número {numero} é negativo.")

