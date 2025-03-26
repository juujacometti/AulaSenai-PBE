# Solicite ao usuário para inserir um número e diga se ele é par ou ímpar

numero = int(input("Digite um número inteiro para verificar se o mesmo é ímpar ou par:\n"))

if numero % 2 == 0:
    print(f"O número {numero} é par!")

else:
    print(f"O número {numero} é ímpar!")

