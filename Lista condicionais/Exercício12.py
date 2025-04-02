# Solicite ao usuário três números e diga se estão em ordem crescente, decrescente ou se são iguais.

numero1 = int(input("Digite um número inteiro:\n"))
numero2 = int(input("Digite um segundo número inteiro:\n"))
numero3 = int(input("Digite um terceiro número inteiro:\n"))

if numero1 > numero2 and numero2 > numero3:
    print(f"Todos os números estão em ordem CRESCENTE.")
elif numero1 < numero2 and numero2 < numero3:
    print(f"Todos os números estão em ordem DECRESCENTE.")
elif numero1 > numero2 and numero2 == numero3:
    print(
        f"O número {numero1} e o número {numero2} estão em ordem CRESCENTE. O número {numero2} e o número {numero3} são IGUAIS.")
elif numero1 < numero2 and numero2 == numero3:
    print(
        f"O número {numero1} e o número {numero2} estão em ordem DECRESCENTE. O número {numero2} e o número {numero3} são IGUAIS.")
elif numero1 == numero2 and numero2 > numero3:
    print(
        f"O número {numero1} e o número {numero2} são IGUAIS. O número {numero2} e o número {numero3} estão em ordem CRESCENTE.")
elif numero1 == numero2 and numero2 < numero3:
    print(
        f"O número {numero1} e o número {numero2} são IGUAIS. O número {numero2} e o número {numero3} estão em ordem DECRESCENTE.")
elif numero1 == numero2 and numero2 == numero3:
    print(f"Todos os números são IGUAIS.")