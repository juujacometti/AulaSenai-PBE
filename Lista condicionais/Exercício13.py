'''
Pergunte ao usuário a temperatura em Celsius e classifique como:
Frio (abaixo de 10°C), Aconchegante (10°C a 25°C), Quente (25°C a 40°C), Muito Quente (acima de 40°C)
'''

temperatura = int(input("Digite a temperatura en graus Celsius para verificara a classificação:\n"))

if temperatura > 40:
    print("Classificação: Muito quente")

elif temperatura >= 25 and temperatura < 40:
    print("Classificação: Quente")

elif temperatura >= 10 and temperatura < 25:
    print("Classificação: Aconchegante")

elif temperatura < 10:
    print("Classificação: Frio")