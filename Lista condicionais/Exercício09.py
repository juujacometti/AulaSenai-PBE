'''
Solicite ao usuário o valor total de uma compra e calcule o desconto de acordo com o valor: 
• Menos de R$ 100: 5% de desconto
• Entre R$ 100 e R$ 500: 10% de desconto
• Mais de R$ 500: 15% de desconto
'''

valor_compra = float(input("Digite o valor da sua compra para descobrir a quantidade de desconto:\n"))

if valor_compra < 100:
    desconto = valor_compra * 0.05
    print(f"O valor da sua compra foi de: R${valor_compra}\nDesconto de: 5%\nValor da compra com desconto: R${valor_compra - desconto}")

elif valor_compra >= 100 and valor_compra <= 500:
    desconto = valor_compra * 0.10
    print(f"O valor da sua compra foi de: R${valor_compra}\nDesconto de: 10%\nValor da compra com desconto: R${valor_compra - desconto}")

elif valor_compra > 500:
    desconto = valor_compra * 0.15
    print(f"O valor da sua compra foi de: R${valor_compra}\nDesconto de: 15%\nValor da compra com desconto: R${valor_compra - desconto}")
