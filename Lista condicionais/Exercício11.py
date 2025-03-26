'''
Pergunte ao usuário o peso e a altura e calcule o IMC. Classifique conforme os resultados: 
• Abaixo de 18.5: Abaixo do peso
• Entre 18.5 e 24.9: Peso normal
• Entre 25 e 29.9: Sobrepeso
• Acima de 30: Obesidade
'''

peso = float(input("Digite seu peso (em kg):\n"))
altura = float(input("Digite sua altura (em metros):\n"))

imc = peso / (altura**2)

if (imc < 18.5):
    print(f"\nO resultado do seu IMC é = {imc}.\nClassificação: ABAIXO DO PESO")

elif (imc >= 18.5 and imc <= 24.9):
    print(f"\nO resultado do seu IMC é = {imc}.\nClassificação: PESO NORMAL")
    
elif (imc >= 25 and imc <= 29.9):
    print(f"\nO resultado do seu IMC é = {imc}.\nClassificação: SOBREPESO")
    
elif imc > 30:
    print(f"\nO resultado do seu IMC é = {imc}.\nClassificação: OBESIDADE")
