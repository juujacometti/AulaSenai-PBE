# Crie duas variáveis, num1 e num2, com valores solicitados ao usuário, respectivamente. Verifique se num1 é maior que num2 e imprima o resultado (True ou False). SEM USAR IF-ELIF-ELSE

num1 = int(input("Digite um número inteiro:\n"))
num2 = int(input("Digite um segundo número inteiro:\n"))

print("\nCaso o resultado seja TRUE, significa que o primeiro número escolhido é maior que o segundo.\nCaso seja FALSE, significa que o primeiro número escolhido é menor que o segundo número.\n")
print(f"Resultado: {num1 > num2}")
