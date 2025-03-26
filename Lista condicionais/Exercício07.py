# Pergunte ao usuário a sua idade e informe se ele tem direito a um desconto (crianças até 12 anos, adultos entre 13 e 59 anos, idosos a partir de 60 anos).

idade = int(input("Digite a sua idade:\n"))

if idade <=12:
    print("Classificação: CRIANÇA\nPossui direito a desconto!")

elif idade >= 13 and idade <= 59:
    print("Classificação: ADULTO\nNão possui direito a desconto.")

else: 
    print("Classificação: IDOSO\nPossui direito a desconto!")