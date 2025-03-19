# Crie uma variável preco com o valor escolhido pelo usuário. Converta esse valor para uma string e concatene com a string "O preço é R$". Imprima o resultado.

preco = float(input("Digite o preço do produto:\n"))

produto = str(preco)

print("O preço do produto é: R$" + produto)