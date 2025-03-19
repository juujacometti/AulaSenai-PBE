#  Crie três variáveis, nota1, nota2 e nota3, com valores escolhidos pelo usuário. Calcule a média ponderada dessas notas, onde os pesos são 2, 3 e 5, respectivamente. Imprima o resultado

nota1 = float(input("Digite o valor da primeira nota:\n"))
nota2 = float(input("Digite o valor da segunda nota:\n"))
nota3 = float(input("Digite o valor da terceira nota:\n"))

media_ponderada = ((nota1 + 2) + (nota2 + 3) + (nota3 + 5)) / (2 + 3 + 5)

print(f"A média ponderada das notas informadas é = {media_ponderada}")
